class Task:
    'Common base class for all task'
    def __init__(self, name, department, skillSet, difficulty, length, activeEmployees, description, priority, assigned):
        self.name = name
        self.department =department
        self.skillSet = skillSet
        self.difficulty = difficulty
        self.length = length
        self.activeEmployees = activeEmployees
        self.description = description
        self.priority = priority

    def __str__ (self):
        print ("Task: \n   Name:            ", self.name,
                     "\n   Description:     ", self.description,
                     "\n   Department:      ", self.department,
                     "\n   Skill Set:       ", self.skillSet,
                     "\n   Difficulty:      ", self.difficulty,
                     "\n   Length:          ", self.length,
                     "\n   Active Employee: ", self.activeEmployees,
                     "\n   Priority:        ", self.priority
               )
