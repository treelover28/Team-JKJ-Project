class Task:
    'Common base class for all task'
    def __init__(self, name, department, skillSet, difficulty, length, description, priority, assignedNeeded):
        self.name = name
        self.department = department
        self.skillSet = skillSet
        self.difficulty = difficulty
        self.length = length
        self.description = description
        self.priority = priority
        self.assignedNeeded = assignedNeeded

    def __str__ (self):
        return "{}".format(self.name)
