
import collections
# from PriorityQueue import PriorityQueue


class Employee(object):
    # def __init__(self, firstName: str, lastName: str, department: [], skillSet: [], activeJobs: [], capacity: int):
    #     self.firstName = firstName
    #     self.lastName = lastName
    #     self.department = department
    #     self.skillSet = skillSet
    #     self.activeJobs = PriorityQueue(activeJobs)
    #     self.capacity = capacity
    def __init__(self, firstName: str, lastName: str, department: [], skillSet: [], capacity: int):
        self.firstName = firstName
        self.lastName = lastName
        self.department = department
        self.skillSet = skillSet
        # self.activeJobs = PriorityQueue(activeJobs)
        self.capacity = capacity

    def __str__ (self):
        print ("Task: \n	FirstName:	", self.firstName,
                     "\n	Last Name:	", self.lastName,
                     "\n	Department:	", self.department,
                     "\n	Skill Set:	", self.skillSet,
                     "\n	Capacity:	", self.capacity,
               )

# if __name__ == "__main__":
#     employee = Employee("Alo", "Oke", ["IT", "IT2"], [
#                         "123", "456"], [1, 2, 3, 4], 100)
#     print(employee)
