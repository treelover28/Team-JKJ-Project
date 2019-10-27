from Employee import Employee
from Task import Task
from PriorityQueue import PriorityQueue

class JobAssignment(object):
	# return # of matching entries between 2 lists
	def compareList(self, list1: [], list2: []):
		appeared = {}
		for entry in list1:
			appeared[entry] = 1

		numMatched = 0

		for entry in list2:
			if entry in appeared:
				numMatched = numMatched + 1

		return numMatched

	def evaluation(self, matchDept: int, matchSkill: int, capacity: int):
		return 1 * matchDept + 1 * matchSkill + 1 * capacity
		# weight1 * matchDept + weight2 * matchSkill + weight3 * capacity

	def getAssignment(self, task: Task, employeeList: [], maxCapacity: int):
		availableEmployee = employeeList
		PQ = PriorityQueue([])

		for employee in availableEmployee:
			matchDept = compareList(employee.department, task.department)
			matchSkill = compareList(employee.skillSet, task.skillSet)

			if employee.capacity >= maxCapacity or matchDept == 0 or matchSkill == 0:
				availableEmployee.remove(employee)

			PQ.add((evaluation(matchDept, matchSkill, capacity - employee.capacity), employee))

		assignedEmployee = []

		for i in range(max(len(availableEmployee), task.assignedNeeded)):
			assignedEmployee.append(PQ.pop()[1])

		return assignedEmployee

		