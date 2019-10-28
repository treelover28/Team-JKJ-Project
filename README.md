# Team-JKJ-Project
# Project Name
## What problem does my app solve?
Most entrepreneurs when starting their business usually face the difficulty of managing employees to make the business function properly. Specifically, startups usually have their employees with different skillsets working in multiple departments, and it is difficult to efficiently assign jobs to the correct employees, especially when the task requires a large number of skillsets and multiple employees to finish. <br />
## How does my app solve the problem?
Name is an employee management application that aims to efficiently assign current tasks to available employees and report back to the employer. Specifically, the program takes in a database containing information (department, skillset, and current active tasks) of available employees. The program also takes in a list of task which containing the description, the difficulty, the length, the description, the department, and the skillset required. The algorithm will process the information and use priority queues to assign the perfect employees for each task so that everybody should have the same amount of work and also be suitable for their assigned tasks.<br/>
## Instructions
Step 1: Make sure you download mongoDB and have it installed on your computer <br/>
Step 2: You have to install the Python modules:<br/>
* json
* pymongo
* requests
* eve (Python Eve framework)
* tkinter <br/>
Step 3: Make sure you turn on mongoDB server first. On Windows, type on terminal <pre> mongod </pre> On Linux, type on terminal <pre> sudo mongod </pre> <br/>
Step 4: Run jkjapp.py in terminal to turn on the app (It is expected to not open any windows. It just lets the app run in background)<br/>
Step 5: Run GUI.py to access GUI.<br/>