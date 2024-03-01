def addtask():
    task.append(input("Enter the task:"))
    print("Task added succesfully")
def viewtask():
    if not task:
        print("NO tasks")
    else:
        for index,i in enumerate(task,start=1):
            print(f"{index}.{i}")
def marked():
    pos=int(input("Enter a position"))
    if 1<=pos<=len(task):
        task[pos-1]="Completed"
        print("Task completed")
    else:
        print("Invalid position")
def delete():
    pos=int(input("Enter the position"))
    if 1<=pos<=len(task):
        del task[pos-1]
        print("Task is deleted")
    else:
        print("Invalid position")
task=[]
while True:
    print("Menu")
    print("1.Add task")
    print("2.View task")
    print("3.Mark as complete")
    print("4.delete")
    print("5.exit")
    ch=int(input("Enter the choice"))
    if ch==1:
        addtask()

    elif ch==2:
        viewtask()
    elif ch==3:
        marked()
    elif ch==4:
        delete()
    elif ch==5:
        print("Thank you")
        exit()
    else:
        print("Invalid choice")