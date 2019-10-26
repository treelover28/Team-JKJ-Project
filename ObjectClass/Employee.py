
import collections
import PriorityQueue

class Employee(object):
	def __init__(self, department: [], skillSet: [], activeJobs: [], capacity: int):
		self.department = department
		self.skillSet = skillSet
		self.activeJobs = PriorityQueue(activeJobs)
		self.capacity = capacity