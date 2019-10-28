#simple GUI

import tkinter as tk
from tkinter import messagebox
from Task import Task
from Employee import Employee
from settings import employees_schema
from settings import tasks_schema
from client import client
from JobAssignment import JobAssignment

connection = client()

HEIGHT = 700
WIDTH = 1200
#create the window
root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width =WIDTH )
canvas.pack()

#modify root window
root.title("Simple GUI")



#frame

frameEmp = tk.Frame(root, bg = '#adede0')
frameEmp.place(rely = 0, relx =0, relwidth = 1/3, relheight =4/7)

frameTask = tk.Frame(root, bg = '#9df5b9')
frameTask.place(rely =0, relx = 1/3, relwidth = 1/3, relheight = 4/7)

frameManual = tk.Frame(root, bg = '#edff91')
frameManual.place(rely = 0, relx = 2/3, relwidth = 1/3, relheight = 4/7)

frameAssign = tk.Frame(root, bg = '#9bddfa')
frameAssign.place(rely = 4/7, relx = 0, relwidth = 5/12, relheight =3/7)

frameResult = tk.Frame(root, bg = '#ffbddb')
frameResult.place(rely = 4/7, relx = 5/12, relwidth = 7/12, relheight =3/7)

# frame for adding Employee
label1 = tk.Label(frameEmp, text = "Add new employees", bg = '#adede0', font=("Roboto", 16))
label1.place(x = 100, y = 0, height  = 40, width =200)

label2 = tk.Label(frameEmp, text = "First Name", bg = '#adede0', font=("Roboto", 11))
label2.place(x = 20, y = 45, height  = 40, width =80)

entry1 = tk.Entry(frameEmp, bd = 5)
entry1.place(x = 110, y = 45, height  = 40, width =250)

label3 = tk.Label(frameEmp, text = "Last Name", bg = '#adede0', font=("Roboto", 11))
label3.place(x = 20, y = 90, height  = 40, width =80)

entry2 = tk.Entry(frameEmp, bd = 5)
entry2.place(x = 110, y = 90, height  = 40, width =250)

label4 = tk.Label(frameEmp, text = "Department", bg = '#adede0', font=("Roboto", 11))
label4.place(x = 20, y = 135, height  = 40, width =80)
list1 = tk.Listbox (frameEmp, font=("Roboto", 11), selectmode = tk.MULTIPLE,exportselection=0)
scroll1 = tk.Scrollbar (frameEmp, command = list1.yview)
list1.configure(yscrollcommand = scroll1.set)
list1.place (x = 110, y = 135, height = 75, width = 250)
scroll1.place(x=335, y =135, height = 75, width =25)

for q in (employees_schema['department'])['allowed']:
    list1.insert(tk.END, q)

label5 = tk.Label(frameEmp, text = "SkillSet", bg = '#adede0', font=("Roboto", 11))
label5.place(x = 20, y = 240, height  = 40, width =80)
list2 = tk.Listbox (frameEmp, font=("Roboto", 11), selectmode = tk.MULTIPLE, exportselection=0)
scroll2 = tk.Scrollbar (frameEmp, command = list2.yview)
list2.configure(yscrollcommand = scroll2.set)
list2.place (x = 110, y = 215, height = 75, width = 250)
scroll2.place(x=335, y =215, height = 75, width =25)

for q in (employees_schema['skillset'])['allowed']:
    list2.insert(tk.END, q)

label6 = tk.Label(frameEmp, text = "Capacity", bg = '#adede0', font=("Roboto", 11))
label6.place(x = 20, y = 295, height  = 40, width =80)
entry3 = tk.Entry(frameEmp, bd = 5)
entry3.place(x = 110, y = 295, height  = 40, width =250)



def addEmp():
    empFName = entry1.get()
    empLName = entry2.get()
    listIndex = list1.curselection()
    listDep = []
    for i in listIndex:
        listDep.append(list1.get(i))
    listIndex = list2.curselection()
    listSkill = []
    for i in listIndex:
        listSkill.append(list2.get(i))
    cap = entry3.get()
    emp = Employee(empFName, empLName, listDep, listSkill, cap)
    connection.post_employee(emp)
    list32.delete(0, tk.END)
    for q in connection.get_all_employees(returnObject=True):
        list32.insert(tk.END, q)
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    list1.delete(0, tk.END)
    for q in (employees_schema['department'])['allowed']:
        list1.insert(tk.END, q)
    list2.delete(0, tk.END)
    for q in (employees_schema['skillset'])['allowed']:
        list2.insert(tk.END, q)
    messagebox.showinfo("Message", "Employee added")

B1 = tk.Button(frameEmp, text ="Add Employee", command = addEmp, font=("Roboto", 11))
B1.place (x =150, y = 355, height = 40, width = 100)

# frame for adding Task
label21 = tk.Label(frameTask, text = "Add new task", bg = '#9df5b9', font=("Roboto", 16))
label21.place(x = 100, y = 0, height  = 30, width =200)

label22 = tk.Label(frameTask, text = "Task Name", bg = '#9df5b9', font=("Roboto", 11))
label22.place(x = 20, y = 35, height  = 30, width =80)
entry21 = tk.Entry(frameTask, bd = 5)
entry21.place(x = 110, y = 35, height  = 30, width =250)

label23 = tk.Label(frameTask, text = "Department", bg = '#9df5b9', font=("Roboto", 11))
label23.place(x = 20, y = 70, height  = 30, width =80)
list21 = tk.Listbox (frameTask, font=("Roboto", 11), selectmode = tk.MULTIPLE,exportselection=0)
scroll21 = tk.Scrollbar (frameTask, command = list21.yview)
list21.configure(yscrollcommand = scroll21.set)
list21.place (x = 110, y = 70, height = 50, width = 250)
scroll21.place(x=335, y =70, height = 50, width =25)

for q in (tasks_schema['department'])['allowed']:
    list21.insert(tk.END, q)

label24 = tk.Label(frameTask, text = "Skillset", bg = '#9df5b9', font=("Roboto", 11))
label24.place(x = 20, y = 125, height  = 30, width =80)
list22 = tk.Listbox (frameTask, font=("Roboto", 11), selectmode = tk.MULTIPLE,exportselection=0)
scroll22 = tk.Scrollbar (frameTask, command = list22.yview)
list22.configure(yscrollcommand = scroll22.set)
list22.place (x = 110, y = 125, height = 50, width = 250)
scroll22.place(x=335, y =125, height = 50, width =25)

for q in (tasks_schema['skillset'])['allowed']:
    list22.insert(tk.END, q)

label25 = tk.Label(frameTask, text = "Difficulty", bg = '#9df5b9', font=("Roboto", 11))
label25.place(x = 20, y = 180, height  = 30, width =80)
spinBox21 = tk.Spinbox(frameTask, from_ = 1, to = 10, font=("Roboto", 11))
spinBox21.place(x = 110, y = 180, height  = 30, width =250)

label26 = tk.Label(frameTask, text = "Length", bg = '#9df5b9', font=("Roboto", 11))
label26.place(x = 20, y = 215, height  = 30, width =80)
SpinBox22 = tk.Spinbox(frameTask, from_ = 1, to = 200, font=("Roboto", 11))
SpinBox22.place(x = 110, y = 215, height  = 30, width =250)

label27 = tk.Label(frameTask, text = "Description", bg = '#9df5b9', font=("Roboto", 11))
label27.place(x = 20, y = 250, height  = 30, width =80)
entry24 = tk.Entry(frameTask, bd = 5)
entry24.place(x = 110, y = 250, height  = 30, width =250)

label28 = tk.Label(frameTask, text = "Priority", bg = '#9df5b9', font=("Roboto", 11))
label28.place(x = 20, y = 285, height  = 30, width =80)
spinBox23 = tk.Spinbox(frameTask, from_ = 1, to = 10, font=("Roboto", 11))
spinBox23.place(x = 110, y = 285, height  = 30, width =250)

label29 = tk.Label(frameTask, text = "Employees", bg = '#9df5b9', font=("Roboto", 11))
label29.place(x = 20, y = 320, height  = 30, width =80)
label30 = tk.Label(frameTask, text = "Needed", bg = '#9df5b9', font=("Roboto", 11))
label30.place(x = 20, y = 345, height  = 30, width =80)
spinBox24 = tk.Spinbox(frameTask, from_ = 1, to = 100, font=("Roboto", 11))
spinBox24.place(x = 110, y = 320, height  = 30, width =250)

def addTask():
    taskName = entry21.get()
    diff = spinBox21.get()
    l = SpinBox22.get()
    descript = entry24.get()
    empNeeded = spinBox24.get()
    priority = spinBox23.get()
    listIndex =  list21.curselection()
    listDep = []
    for i in listIndex:
        listDep.append(list21.get(i))
    listIndex = list22.curselection()
    listSkill = []
    for i in listIndex:
        listSkill.append(list22.get(i))
    task = Task(taskName, listDep, listSkill, diff, l, descript, priority, empNeeded)
    connection.post_tasks(task)
    list31.delete(0, tk.END)
    for q in connection.get_all_tasks(threshold = 0, returnObject = True):
        list31.insert(tk.END, q)
    list41.delete(0,tk.END)
    for q in connection.get_all_tasks(threshold = 0, returnObject= True):
        list41.insert(tk.END, q)
    entry21.delete(0, tk.END)
    entry24.delete(0, tk.END)
    list21.delete(0, tk.END)
    list22.delete(0, tk.END)
    for q in (tasks_schema['department'])['allowed']:
        list21.insert(tk.END, q)
    for q in (tasks_schema['skillset'])['allowed']:
        list22.insert(tk.END, q)
    messagebox.showinfo("Message", "Task added")

B2 = tk.Button(frameTask, text ="Add Task", command = addTask, font=("Roboto", 11))
B2.place (x =150, y = 355, height = 40, width = 100)

# frame for Manual Task Assignment
label31 = tk.Label(frameManual, text = "Manual Task Assignment", bg = '#edff91', font=("Roboto", 16))
label31.place(x = 50, y = 0, height  = 40, width =300)

label32 = tk.Label(frameManual, text = "Task", bg = '#edff91', font=("Roboto", 11))
label32.place(x = 20, y = 45, height  = 40, width =80)
list31 = tk.Listbox (frameManual, font=("Roboto", 11), selectmode = tk.SINGLE,exportselection=0)
scroll31 = tk.Scrollbar (frameManual, command = list31.yview)
list31.configure(yscrollcommand = scroll31.set)
list31.place (x = 110, y = 45, height = 150, width = 250)
scroll31.place(x=335, y =45, height = 150, width =25)



for q in connection.get_all_tasks(threshold = 0, returnObject = True):
    list31.insert(tk.END, q)


label33 = tk.Label(frameManual, text = "Employee", bg = '#edff91', font=("Roboto", 11))
label33.place(x = 20, y = 200, height  = 40, width =80)
list32 = tk.Listbox (frameManual, font=("Roboto", 11), selectmode = tk.MULTIPLE,exportselection=0)
scroll32 = tk.Scrollbar (frameManual, command = list32.yview)
list32.configure(yscrollcommand = scroll32.set)
list32.place (x = 110, y = 200, height = 150, width = 250)
scroll32.place(x=335, y =200, height = 150, width =25)

for q in connection.get_all_employees(returnObject=True):
    list32.insert(tk.END, q)

def manualAssign():
    listIndex = list31.curselection()
    taskName = list31.get(listIndex[0])
    listIndex =list32.curselection()
    listEmp = []
    for i in listIndex:
        listEmp.append(list32.get(i))
    # for i in listEmp:
    #     connection.assignTask(connection, )
    list31.delete(0, tk.END)
    list32.delete(0, tk.END)
    for q in range(20):
        list31.insert(tk.END, q)
    for q in range(20):
        list32.insert(tk.END, q)
    messagebox.showinfo("Message", "Task assigned")
B3 = tk.Button(frameManual, text ="Assign", command = manualAssign, font=("Roboto", 11))
B3.place (x =150, y = 355, height = 40, width = 100)

#frame for auto assignment
label41 = tk.Label(frameAssign, text = "Auto Task Assignment", bg = '#9bddfa', font=("Roboto", 16))
label41.place(x = 50, y = 0, height  = 40, width =400)

label42 = tk.Label(frameAssign, text = "Task", bg = '#9bddfa', font=("Roboto", 11))
label42.place(x = 20, y = 50, height  = 40, width =80)
list41 = tk.Listbox (frameAssign, font=("Roboto", 11), selectmode = tk.MULTIPLE,exportselection=0)
scroll41 = tk.Scrollbar (frameAssign, command = list41.yview)
list41.configure(yscrollcommand = scroll41.set)
list41.place (x = 110, y = 50, height = 175, width = 350)
scroll41.place(x=435, y = 50, height = 175, width =25)

for q in connection.get_all_tasks(threshold = 0, returnObject= True):
    list41.insert(tk.END, q)

def autoAssign():
    listIndex = list41.curselection()
    listTask = []
    for i in listIndex:
        listTask.append(list41.get(i))
    
    tasks = []

    for taskName in listTask:
        task = connection.selectTask(taskName, returnObject=True)
        tasks.append(task)

    employees = connection.get_all_employees(returnObject=True)

    assignmentObject = JobAssignment()
    assignedList = assignmentObject.getAssignment(tasks, employees)

    for entry in assignedList:
        connection.assignTask(entry[1][2].firstName, entry[1][2].lastName, entry[0][1].name)

    list41.delete(0, tk.END)
    for q in connection.get_all_tasks(threshold = 0, returnObject= True):
        list41.insert(tk.END, q)
    
    list51.delete(0, tk.END)
    for q in connection.get_all_tasks(threshold = 0, returnObject= True, greaterThan=True):
        list51.insert(tk.END, q)
    messagebox.showinfo("Message", "Task assigned")
B4 = tk.Button(frameAssign, text ="Assign", command = autoAssign, font=("Roboto", 11))
B4.place (x =200, y = 235, height = 40, width = 100)

# frame for result
label51 = tk.Label(frameResult, text = "Assigned Task", bg = '#ffbddb', font=("Roboto", 16))
label51.place(x = 100, y = 0, height  = 40, width =150)

label52 = tk.Label(frameResult, text = "Employee Assigned To Task", bg = '#ffbddb', font=("Roboto", 16))
label52.place(x = 375, y = 0, height  = 40, width =300)

list51 = tk.Listbox (frameResult, font=("Roboto", 11), selectmode = tk.SINGLE,exportselection=0)
scroll51 = tk.Scrollbar (frameResult, command = list51.yview)
list51.configure(yscrollcommand = scroll51.set)
list51.place (x = 20, y = 50, height = 175, width = 310)
scroll51.place(x= 305, y = 50, height = 175, width =25)

for q in connection.get_all_tasks(0, greaterThan=True, returnObject=True):
    list51.insert(tk.END, q)

list52 = tk.Listbox (frameResult, font=("Roboto", 11), selectmode = tk.SINGLE,exportselection=0)
scroll52 = tk.Scrollbar (frameResult, command = list52.yview)
list52.configure(yscrollcommand = scroll52.set)
list52.place (x = 370, y = 50, height = 175, width = 310)
scroll52.place(x= 655, y = 50, height = 175, width =25)

def seeAssigned():
    listIndex = list51.curselection()
    taskName = list51.get(listIndex[0])
    list52.delete(0, tk.END)
    for q in connection.get_tasks_assignees(taskName, returnName=True):
        list52.insert(tk.END, q)

B5 = tk.Button(frameResult, text = "See Employees Assigned", command = seeAssigned, font=("Roboto", 11))
B5.place (x =75, y = 235, height = 40, width = 200)


#kick off the event loopo
root.mainloop()
