
import collections
import PriorityQueue

class Employee(object):
	def __init__(self, firstName: str, lastName: str, department: [], skillSet: [], activeJobs: [], capacity: int):
		self.firstName = firstName
		self.lastName = lastName
		self.department = department
		self.skillSet = skillSet
		self.activeJobs = PriorityQueue(activeJobs)
		self.capacity = capacity