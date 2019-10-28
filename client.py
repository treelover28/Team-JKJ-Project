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
        self.my_client= pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.my_client["jkjDB"]

    def url_for(self, endpoint):
        '''
        Establish connection to particular endpoint in API
        Argument:
            endpoint (str) : name of endpoint
        Return url to endpoint
        '''
        return 'http://localhost:5000/{}/'.format(endpoint)

    def delete_all_tasks(self):
        ''' 
        Void method. 
        Argument:
            No argument.
        Delete all tasks in current 'task' endpoint. \\
        Return 204 if successful. \\
        Return error code if URL is invalid or endpoint is already empty
        '''
        r = requests.delete(self.url_for("tasks"))
        # if deletion is unsuccesful return error code
        if r.status_code != 204 :
            print("Error occured with delete_all_tasks(). Server response:", r.status_code,...
            and "\nEither URL is invalid or enpoint is already empty.")
        else:
            print("All tasks have been removed. Server response: ", r.status_code)

    def delete_all_employees(self):
        ''' 
        Void method. 
        Argument:
            No argument.
        Delete all tasks in current 'employee' endpoint. \\
        Return 204 if successful. \\
        Return error code if URL is invalid or endpoint is already empty
        '''
        r = requests.delete(self.url_for("employees"))
        if (r.status_code != 404):
            print("All employees have been removed. Status code: ", r.status_code)
        else:
            print("Error occured with delete_all_employees(). Server response:", r.status_code,...
            and "\nEither URL is invalid or enpoint is already empty.")

    def post_employee(self, employee : Employee):
        '''
        Void. Takes in Employee object and post object to "employees" endpoint. \\
        Argument: 
            employee (Employee) : employee to be posted on "employees" endpoint\\
        
        Print status code and message afterward
        '''
        data = {
            "firstName" : employee.firstName,
            "lastName" : employee.lastName,
            "department" : employee.department,
            "skillset" : employee.skillSet,
            # active_jobs is empty by default
            "capacity" : 0
        }

        r = requests.post(
            self.url_for("employees"), 
            json.dumps(data), 
            headers= {"Content-Type" : "application/json"}
        )
        if (r.status_code != 201):
            print("Error occured with post_employee(). Status code: " , r.status_code, "\n", r.text)
        else:
            print("Employee posted successfully. Status code: ", r.status_code)

    def post_tasks(self, task: Task):
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
            "assignee_needed" : task.assignedNeeded,
            # list of active employees is empty by default :
            "priority" : task.priority,
            "num_assignees" : 0
        }

        r = requests.post(
            self.url_for("tasks"), 
            json.dumps(data), 
            headers= {"Content-Type" : "application/json"}
        )
        if (r.status_code != 201):
            print("Error occured with post_task(). Status code: " , r.status_code, "\n", r.text)
        else:
            print("Task posted successfully. Status code: ", r.status_code)


    def selectEmployee(self, firstName: str, lastName: str):
        '''
        Query "employees" endpoint to find employee with matching name. \\
        Argument:
            firstName (str) : first name of employee \\
            lastName (str) : last name of employee \\ 
        return JSON-dictionary should it find the matching employee. \\
        return None if not found
        '''
        employeeQuery = {"firstName" : firstName, "lastName" : lastName}
        result = self.db["employees"].find_one(employeeQuery)
        # print(result["_id"])
        return result

    def selectTask(self, taskName: str, returnObject: bool = False):
        '''
        Query "tasks" endpoint to find task with matching name. \\
        Argument:
            taskName (str) : name of tasks \\
        return JSON-dictionary should it find the matching task. \\
        return None if not found
        '''
        taskQuery = {"name" : taskName}
        i = self.db["tasks"].find_one(taskQuery)
        # print(result["_id"])
        if (returnObject is True):
            task = Task(i["name"], i["department"],i["skillset"], i["difficulty"], i["length"], i["description"], i["priority"], i["num_assignees"])
            return task
        else:
            return i

    def assignTask(self,firstName: str, lastName: str, taskName: str):
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
        employee = self.selectEmployee(firstName, lastName)
        task = self.selectTask(taskName)
        if (employee is not None and task is not None):
            self.db["employees"].update_one(employee, {'$push' : {"active_jobs" : task["_id"]}})
            self.db["tasks"].update_one(task, {"$push" : {"active_employees" : employee["_id"]}})

            # increment the capacity of current employee 
            self.db["employees"].update_one({"_id" : employee["_id"]}, {'$inc' : {"capacity" : 1}}, upsert= False)
            # increment the number of assignees on current task 
            self.db["tasks"].update_one({"_id" : task["_id"]}, {'$inc' : {"num_assignees" : 1}}, upsert= False)
        else:
            print("Error occured while assigning task. Either employee doesn't exist or task doesn't exists on their respective endpoints.")

    def removeTask(self,firstName: str, lastName: str, taskName: str):
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
        employee = self.selectEmployee(firstName, lastName)
        task = self.selectTask(taskName)
        if (employee is not None and task is not None):
            self.db["employees"].update(employee, {'$pull' : {"active_jobs" : task["_id"]}})
            self.db["tasks"].update(task, {"$pull" : {"active_employees" : employee["_id"]}})

            # decrement the capacity of current employee 
            self.db["employees"].update_one({"_id" : employee["_id"]}, {'$inc' : {"capacity" : -1}}, upsert= False)
            # decrement the number of assignees on current task 
            self.db["tasks"].update_one({"_id" : task["_id"]}, {'$inc' : {"num_assignees" : -1}}, upsert= False)
        else:
            print("Error occured while removing task. Either employee doesn't exist or task doesn't exists on their respective endpoints.")


    def get_employees_tasks(self, firstName: str, lastName: str, returnName: bool = False):
        '''
        Return a list of specified employee's active jobs
        Argument:
            firstName (str) : first name of employee \\
            lastName (str) : last name of employee \\
            returnName (bool) : choice to return task name instead of ObjectId
        '''
        taskList = self.selectEmployee(firstName, lastName)["active_jobs"]
        
        if (returnName is True): # we will return the task names instead of objectid
            res = []
            for task in taskList:
                title = self.db["tasks"].find_one({"_id" : task})["name"]
                res.append(title) 
            taskList = res
        return taskList

    def get_tasks_assignees(self, taskName: str, returnName : bool = False):
        '''
        Return a list of current assignee working on a specified task
        Argument:
            taskName (str) : name of task \\
            returnName (bool) : choice to return task name instead of ObjectId
        '''
        employeeList = self.selectTask(taskName)["active_employees"]
        if (returnName is True): # we will return the task names instead of objectid
            res = []
            for e in employeeList:
                firstName = self.db["employees"].find_one({"_id" : e})["firstName"]
                lastName = self.db["employees"].find_one({"_id" : e})["lastName"]
                employee = (firstName, lastName)
                res.append(employee)
            employeeList = res
        return employeeList

    def get_all_employees(self, threshold: int = None, howMany : int = None,returnObject : bool = False ):
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
            temp = self.db["employees"].find()
            for i in range(0, temp.count()):
                employeeList.append(temp[i])
        elif (howMany is None):
            temp = self.db["employees"].find({"capacity": {"$lte" : threshold}})
            for i in range(0, temp.count()):
                employeeList.append(temp[i])

        elif (threshold is None):
            temp = self.db["employees"].find()
            for i in range(0, min(temp.count(), howMany)):
                employeeList.append(temp[i])
        else:
            temp = self.db["employees"].find({"capacity": {"$lte" : threshold}})
            for i in range(0, min(temp.count(),howMany)):
                employeeList.append(temp[i])
        
        if (returnObject is True):
            res = []
            for i in employeeList:
                e = Employee(i["firstName"], i["lastName"],i["department"], i["skillset"],i["capacity"])
                res.append(e)
            return res
        else: 
            return employeeList

    def get_all_tasks(self,threshold: int = None, howMany : int = None, returnObject : bool = False, greaterThan: bool = False):
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
            temp = self.db["tasks"].find()
            for i in range(0, temp.count()):
                taskList.append(temp[i])
        elif (howMany is None):
            if (greaterThan is True):
                temp = self.db["tasks"].find({"num_assignees": {"$gt" : threshold}})
            else:
                temp = self.db["tasks"].find({"num_assignees": {"$lte" : threshold}})
            for i in range(0, temp.count()):
                taskList.append(temp[i])

        elif (threshold is None):
            temp = self.db["tasks"].find()
            for i in range(0, min(temp.count(), howMany)):
                taskList.append(temp[i])
        else:
            if (greaterThan is True):
                temp = self.db["tasks"].find({"num_assignees": {"$gt" : threshold}})
            else:
                temp = self.db["tasks"].find({"num_assignees": {"$lte" : threshold}})
            for i in range(0, min(temp.count(),howMany)):
                taskList.append(temp[i])
        
        if (returnObject is True):
            res = []
            for i in taskList:
                e = Task(i["name"], i["department"],i["skillset"], i["difficulty"], i["length"], i["description"], i["priority"], i["num_assignees"])
                res.append(e)
            return res # object
        else:
            return taskList # references id

def main():
    connection = client()
    connection.delete_all_employees()
    connection.delete_all_tasks()
    employee1 = Employee("Phong","Pham", ["Accounting"], ["IT"],100)
    employee2 = Employee("Chanh","Bui", ["Finance"], ["Data Analytics"],100)
    employee3 = Employee("Khai","Lai", ["IT"], ["Data Analytics"],100)

    task1 = Task("Make GUI", ["IT"], ["Technology"],5,5,"Using something to make GUI lol",5,5)
    task2 = Task("Code Backend", ["IT"], ["Technology"],5,5,"Use Python Eve Framework and MongoDB",5,5)
    task3 = Task("Do Algorithms", ["IT"], ["Technology"],5,5,"Use his 200 IQ brain",5,5)

    connection.post_employee(employee1)
    connection.post_employee(employee2)
    connection.post_employee(employee3)

    connection.post_tasks(task1)
    connection.post_tasks(task2)
    connection.post_tasks(task3)

    connection.assignTask("Phong", "Pham", "Do Algorithms")
    connection.assignTask("Chanh", "Bui", "Make GUI")
    connection.assignTask("Khai", "Lai", "Code Backend")
    connection.assignTask("Phong", "Pham", "Make GUI")

    # print(get_employees_tasks("Phong", "Pham",True))
    print("\n")
    # print(get_tasks_assignees("Make GUI",True))

    # print(get_all_employees(howMany = 4))
    l = connection.get_all_employees()
    for e in l:
        print(e)
    
    l = connection.get_all_tasks()
    for e in l:
        print(e)


    # removeTask("Phong", "Pham", "Make GUI")
if __name__ == "__main__":
    main()

