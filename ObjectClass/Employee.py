
import collections
import PriorityQueue

class Employee(object):
	def __init__(department: [], skillset: [], activeJobs: []):
		self.department = department
		self.skillset = skillset
		self.activeJobs = PriorityQueue(activeJobs)