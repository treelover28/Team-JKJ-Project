
import collections
import PriorityQueue

class Employee(object):
	def __init__(self, department: [], skillset: [], activeJobs: [], capacity: int):
		self.department = department
		self.skillset = skillset
		self.activeJobs = PriorityQueue(activeJobs)
		self.capacity = capacity