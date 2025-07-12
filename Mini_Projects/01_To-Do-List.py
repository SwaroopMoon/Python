def task():#function defination
    tasks = [] #empty list
    print("-----WELCOME TO THE TASK MANAGEMENT APP-----")

    task_count = int(input("Enter the number of tasks:"))
    for i in range(1,task_count+1):
        task_val = input(f"Enter the task {i}:")
        tasks.append(task_val)
    print(f"Your To-Do List is : {tasks}")

    while True:
        operation=int(input("Enter:\n1-Add\n2-Update\n3-Delete\n4-Exit..\n"))

        if operation==1:
            task_val=input("Enter the new task:")
            tasks.append(task_val)
            print("Your task has been successfully added...")
            print(f"Your To-Do List is : {tasks}")
        elif operation == 2:
            val_to_update = input("Enter the task name you want to update:")
            if val_to_update in tasks:
                updated = input("Enter the New Task :")
                index = tasks.index(val_to_update)
                tasks[index] = updated
                print(f"Your task has been Successfully Updated to {updated}...")
                print(f"Your To-Do List is : {tasks}")
        elif operation == 3:
            val_to_delete = input("Enter the task you want to delete:")
            if val_to_delete in tasks:
                index_del= tasks.index(val_to_delete)
                del tasks[index_del]
                print(f"Your task {val_to_delete} has been successfully deleted...")
                print(f"Your To-Do List is : {tasks}")
        elif operation == 4:
            print("Closing the program....")
            break
task()