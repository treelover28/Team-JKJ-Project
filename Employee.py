
import collections
import PriorityQueue

class Employee(object):
	def __init__(self, lastName: str, firstName: str, department: [], skillSet: [], capacity: int):
		self.firstName = firstName
		self.lastName = lastName
		self.department = department
		self.skillSet = skillSet
		self.capacity = capacity