def task():
    tasks = [] #empty list 
    print("____WELCOME TO THE TASK MANAGEMEMNT APP____")

    total_task = int(input("enter how many task you want to add = ")) #5
    for i in range(1, total_task+1):
        tasK_name = input(f"enter task{i} =") #enter task 3 =
        tasks.append(tasK_name)

    print(f"today's tasks are\n{tasks}")

    while True:
        operation = int(input("enter 1-add\n2-update\n3-delete\n4-view\n5-exit/stop/"))
        if operation == 1:
            add = input("enter task you want to add =")
            tasks.append(add)
            print(f"task {add} has been successfully added..")
        elif operation == 2:
            updated_val = input("enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("enter new task = ")
                ind = tasks.index(updated_val) #2
                tasks[ind] = up
                print(f"updated task {up}")


        elif operation == 3:
            dalete_val = input("which task you want to delete = ")
            if  dalete_val in tasks:
                up = input("enter new task = ")
                ind = tasks.index( dalete_val) #2
                del tasks[ind] 
                print(f"taskc{ dalete_val} has been deleted..")

        elif operation == 3:
            delete_val = input("which task you want to delete = ")
            if  delete_val in tasks:
                up = input("enter new task = ")
                ind = tasks.index( ) #2
                del tasks[ind] 
                print(f"taskc{delete_val} has been deleted..")
                
        elif operation == 4:
           print(f"total tasks = {tasks}")

        elif operation == 5:
           print(f"closing the program")
           break 

        else:
            print(f"invalid input")

task()

        

   

