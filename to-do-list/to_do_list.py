'''Features to implement:
o Add a task with a description and deadline.
o View all tasks (sorted by deadline).
o Mark tasks as completed.
o Delete a task.'''
import pandas as pd
import datetime as dt
a =[]

def task():
    global a
    x= "task: "
    y= "deadline: "
    n_tasks = int(input("how many tasks do you want add?: "))
    for i in range(1, n_tasks+1):
        t = input("enter a task: " )
        d = input("enter deadline: ")
        a.append(f"{x}{t} and {y}{d}")
    print(a)
    return a

def write_read():
    with open("task_list.txt", 'w')as f:
     for items in a:
      f.write(f"{items}\n")
    msg_1 = "Here are the tasks."
    print(msg_1)
    for i, j in enumerate(a, start=1):
       print(f"{i}.{j}")
    mark = int(input("Mark one of the above tasks as completed: "))
    a[mark-1] = f"{a[mark-1]}>>this task is completed"
    print(a)
    with open("task_list.txt", 'w') as f:
       for i in a:
          f.write(f"{i}\n")
    return None

def delete_task():
    global a
    message = "Task list: "
    print(message)
    for i,j in enumerate(a, start=1):
       print(f"{i}.{j}")
    delete = int(input("Select a task to delete: "))
    d= delete-1
    a.pop(d)
    with open("task_list.txt", 'w') as f:
       for i in a:
          f.write(f"{i}\n")
    print(a)
    return None

task()
write_read()
delete_task()

    
