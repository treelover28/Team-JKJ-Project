import json 
import requests 
from pprint import pprint
import sys
sys.path.append('../')
from Employee import Employee
from PriorityQueue import PriorityQueue
from Task import Task
import pymongo

# my_client= pymongo.MongoClient("mongodb://localhost:27017/")
# db = my_client["jkjDB"]

class client(object):
    def __init__(self):
        my_client= pymongo.MongoClient("mongodb://localhost:27017/")
        db = my_client["jkjDB"]

    def url_for(endpoint):
        '''
        Establish connection to particular endpoint in API
        Argument:
            endpoint (str) : name of endpoint
        Return url to endpoint
        '''
        return 'http://localhost:5000/{}/'.format(endpoint)

    def delete_all_tasks():
        ''' 
        Void method. 
        Argument:
            No argument.
        Delete all tasks in current 'task' endpoint. \\
        Return 204 if successful. \\
        Return error code if URL is invalid or endpoint is already empty
        '''
        r = requests.delete(url_for("tasks"))
        # if deletion is unsuccesful return error code
        if r.status_code != 204 :
            print("Error occured with delete_all_tasks(). Server response:", r.status_code,...
            and "\nEither URL is invalid or enpoint is already empty.")
        else:
            print("All tasks have been removed. Server response: ", r.status_code)

    def delete_all_employees():
        ''' 
        Void method. 
        Argument:
            No argument.
        Delete all tasks in current 'employee' endpoint. \\
        Return 204 if successful. \\
        Return error code if URL is invalid or endpoint is already empty
        '''
        r = requests.delete(url_for("employees"))
        if (r.status_code != 404):
            print("All employees have been removed. Status code: ", r.status_code)
        else:
            print("Error occured with delete_all_employees(). Server response:", r.status_code,...
            and "\nEither URL is invalid or enpoint is already empty.")

    def post_employee(employee : Employee):
        '''
        Void. Takes in Employee object and post object to "employees" endpoint. \\
        Argument: 
            employee (Employee) : employee to be posted on "employees" endpoint\\
        
        Print status code and message afterward
        '''
        data = {
            "firstName" : emp
    my_client= pymongo.MongoClient("mongodb://localhost:27017/")
    db = my_client["jkjDB"]loyee.firstName,
            "lastName" : employee.lastName,
            "department" : employee.department,
            "skillset" : employee.skillSet,
            # active_jobs is empty by default
            "capacity" : 0
        }

        r = requests.post(
            url_for("employees"), 
            json.dumps(data), 
            headers= {"Content-Type" : "application/json"}
        )
        if (r.status_code != 201):
            print("Error occured with post_employee(). Status code: " , r.status_code, "\n", r.text)
        else:
            print("Employee posted successfully. Status code: ", r.status_code)

    def post_tasks(task: Task):
        '''
        Void. Takes in Task object and post object to "tasks" endpoint. \\
        Argument: 
            task (Employee) : tasks to be posted on "tasks" endpoint\\
        
        Print status code and message afterward
        '''
        data = {
            "name" : task.name,
            "department" : task.department,
            "skillset" : task.skillSet,
            "difficulty" : task.difficulty,
            "length" : task.length,
            "description" : task.description,
            "assignee_needed" : task.assignedNeeded
            # list of active employees is empty by default
        }

        r = requests.post(
            url_for("tasks"), 
            json.dumps(data), 
            headers= {"Content-Type" : "application/json"}
        )
        if (r.status_code != 201):
            print("Error occured with post_task(). Status code: " , r.status_code, "\n", r.text)
        else:
            print("Task posted successfully. Status code: ", r.status_code)


    def selectEmployee(firstName: str, lastName: str):
        '''
        Query "employees" endpoint to find employee with matching name. \\
        Argument:
            firstName (str) : first name of employee \\
            lastName (str) : last name of employee \\ 
        return JSON-dictionary should it find the matching employee. \\
        return None if not found
        '''
        employeeQuery = {"firstName" : firstName, "lastName" : lastName}
        result = db["employees"].find_one(employeeQuery)
        # print(result["_id"])
        return result

    def selectTask(taskName: str):
        '''
        Query "tasks" endpoint to find task with matching name. \\
        Argument:
            taskName (str) : name of tasks \\
        return JSON-dictionary should it find the matching task. \\
        return None if not found
        '''
        taskQuery = {"name" : taskName}
        result = db["tasks"].find_one(taskQuery)
        # print(result["_id"])
        return result 

    def assignTask(firstName: str, lastName: str, taskName: str):
        '''
        Assign specified task to specified employee
        Argument: 
            firstName (str) : first name of employee \\
            lastName (str) : last name of employee \\ 
            taskName (str) : name of task
        Helper functions used:
            selectEmployee : return  dict or None
            selectTask : return dict or None
        Print error message should any problem occur.
        '''
        employee = selectEmployee(firstName, lastName)
        task = selectTask(taskName)
        if (employee is not None and task is not None):
            db["employees"].update_one(employee, {'$push' : {"active_jobs" : task["_id"]}})
            db["tasks"].update_one(task, {"$push" : {"active_employees" : employee["_id"]}})

            # increment the capacity of current employee 
            db["employees"].update_one({"_id" : employee["_id"]}, {'$inc' : {"capacity" : 1}}, upsert= False)
            # increment the number of assignees on current task 
            db["tasks"].update_one({"_id" : task["_id"]}, {'$inc' : {"num_assignees" : 1}}, upsert= False)
        else:
            print("Error occured while assigning task. Either employee doesn't exist or task doesn't exists on their respective endpoints.")

    def removeTask(firstName: str, lastName: str, taskName: str):
        '''
        Remove specified task from specified employee
        Argument: 
            firstName (str) : first name of employee \\
            lastName (str) : last name of employee \\ 
            taskName (str) : name of task
        Helper functions used:
            selectEmployee : return  dict or None
            selectTask : return dict or None
        Print error message should any problem occur.
        '''
        employee = selectEmployee(firstName, lastName)
        task = selectTask(taskName)
        if (employee is not None and task is not None):
            db["employees"].update(employee, {'$pull' : {"active_jobs" : task["_id"]}})
            db["tasks"].update(task, {"$pull" : {"active_employees" : employee["_id"]}})

            # decrement the capacity of current employee 
            db["employees"].update_one({"_id" : employee["_id"]}, {'$inc' : {"capacity" : -1}}, upsert= False)
            # decrement the number of assignees on current task 
            db["tasks"].update_one({"_id" : task["_id"]}, {'$inc' : {"num_assignees" : -1}}, upsert= False)
        else:
            print("Error occured while removing task. Either employee doesn't exist or task doesn't exists on their respective endpoints.")


    def get_employees_tasks(firstName: str, lastName: str, returnName: bool = False):
        '''
        Return a list of specified employee's active jobs
        Argument:
            firstName (str) : first name of employee \\
            lastName (str) : last name of employee \\
            returnName (bool) : choice to return task name instead of ObjectId
        '''
        taskList = selectEmployee(firstName, lastName)["active_jobs"]
        
        if (returnName is True): # we will return the task names instead of objectid
            res = []
            for task in taskList:
                title = db["tasks"].find_one({"_id" : task})["name"]
                res.append(title) 
            taskList = res
        return taskList

    def get_tasks_assignees(taskName: str, returnName : bool = False):
        '''
        Return a list of current assignee working on a specified task
        Argument:
            taskName (str) : name of task \\
            returnName (bool) : choice to return task name instead of ObjectId
        '''
        employeeList = selectTask(taskName)["active_employees"]
        if (returnName is True): # we will return the task names instead of objectid
            res = []
            for e in employeeList:
                firstName = db["employees"].find_one({"_id" : e})["firstName"]
                lastName = db["employees"].find_one({"_id" : e})["lastName"]
                employee = (firstName, lastName)
                res.append(employee)
            employeeList = res
        return employeeList

    def get_all_employees(threshold: int = None, howMany : int = None):
        '''
        Return howMany employees whose capacity <= threshold. \\
        If no argument is provided, return list of all employees. \\
        If only one argument is provided, return the appropriate number of employees who satisfy the argument. \\
        Arguments:
            *optional* threshold (int): you want only the employees whose task list is less than or equal to this threshold 
            *optional* howMany (int) : only return this many of employees, even if more employees were found to satisfy the threshold
        '''
        employeeList = []
        if (threshold is None and howMany is None):
            temp = db["employees"].find()
            for i in range(0, temp.count()):
                employeeList.append(temp[i])
        elif (howMany is None):
            temp = db["employees"].find({"capacity": {"$lte" : threshold}})
            for i in range(0, temp.count()):
                employeeList.append(temp[i])

        elif (threshold is None):
            temp = db["employees"].find()
            for i in range(0, min(temp.count(), howMany)):
                employeeList.append(temp[i])
        else:
            temp = db["employees"].find({"capacity": {"$lte" : threshold}})
            for i in range(0, min(temp.count(),howMany)):
                employeeList.append(temp[i])
        return employeeList

    def get_all_tasks(threshold: int = None, howMany : int = None):
        '''
        Return howMany tasks where their number of assignees <= threshold. \\
        If no argument is provided, return list of all tasks. \\
        If only one argument is provided, return the appropriate number of tasks who satisfy the specifed argument. \\
        Arguments:
            *optional* threshold (int): you want only the tasks where their current number of assignees is less than or equal to this threshold 
            *optional* howMany (int) : only return this many tasks, even if more tasks were found to satisfy the threshold
        '''

        taskList = []
        if (threshold is None and howMany is None):
            temp = db["tasks"].find()
            for i in range(0, temp.count()):
                taskList.append(temp[i])
        elif (howMany is None):
            temp = db["tasks"].find({"num_assignees": {"$lte" : threshold}})
            for i in range(0, temp.count()):
                taskList.append(temp[i])

        elif (threshold is None):
            temp = db["tasks"].find()
            for i in range(0, min(temp.count(), howMany)):
                taskList.append(temp[i])
        else:
            temp = db["tasks"].find({"num_assignees": {"$lte" : threshold}})
            for i in range(0, min(temp.count(),howMany)):
                taskList.append(temp[i])
        return taskList

def main():
    delete_all_employees()
    delete_all_tasks()
    employee1 = Employee("Phong","Pham", ["Accounting"], ["IT"],100)
    employee2 = Employee("Chanh","Bui", ["Finance"], ["Data Analytics"],100)
    employee3 = Employee("Khai","Lai", ["IT"], ["Data Analytics"],100)

    task1 = Task("Make GUI", ["IT"], ["Technology"],5,5,"Using something to make GUI lol",5,5)
    task2 = Task("Code Backend", ["IT"], ["Technology"],5,5,"Use Python Eve Framework and MongoDB",5,5)
    task3 = Task("Do Algorithms", ["IT"], ["Technology"],5,5,"Use his 200 IQ brain",5,5)

    post_employee(employee1)
    post_employee(employee2)
    post_employee(employee3)

    post_tasks(task1)
    post_tasks(task2)
    post_tasks(task3)

    assignTask("Phong", "Pham", "Do Algorithms")
    assignTask("Chanh", "Bui", "Make GUI")
    assignTask("Khai", "Lai", "Code Backend")
    assignTask("Phong", "Pham", "Make GUI")

    # print(get_employees_tasks("Phong", "Pham",True))
    print("\n")
    # print(get_tasks_assignees("Make GUI",True))

    # print(get_all_employees(howMany = 4))
    pprint(get_all_tasks(howMany = 4))


    # removeTask("Phong", "Pham", "Make GUI")
    
    
if __name__ == "__main__":
    main()

