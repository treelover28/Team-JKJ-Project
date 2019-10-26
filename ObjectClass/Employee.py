
import collections
from PriorityQueue import PriorityQueue

class Employee(object):
	def __init__(self, lastName: str, firstName: str, department: [], skillSet: [], activeJobs: [], capacity: int):
		self.firstName = firstName
		self.lastName = lastName
		self.department = department
		self.skillSet = skillSet
		self.activeJobs = PriorityQueue(activeJobs)
		self.capacity = capacity

if __name__ == "__main__":
	employee = Employee("Alo", "Oke", ["IT", "IT2"], ["123", "456"], [1, 2, 3, 4], 100)
	print(employee)