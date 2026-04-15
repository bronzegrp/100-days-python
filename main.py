import time

import json

file_path = r"/home/gryphon_/Todo/" #file can change if working from home :] 

file_name = input("What should the name of the file be: ")

file_path+=file_name

file_path+=".txt"
time.sleep(1)
print(f"Creating file {file_name}")
time.sleep(1)
print("File created")





with open (file_path,"w") as to_do_file:

    app_in_use = True

    
    task_num = 0
    tasks = {}

    title = input("add a title for your task list: ").upper()

    to_do_file.write(f"{title}\n")
    to_do_file.write("\n")

    

    while app_in_use:

        print('Welcome to to do app')
        print('1 to add , 2 to remove , 3 to see tasklist , 4 to complete the tasklist')
        time.sleep(1)
        choice = int(input("What would you like to do: "))

        if choice == 1:
            task_num +=1
            task_to_add = input ("add your task: ") #example -> Do the dishes
            print(f"Adding {task_to_add}")
            time.sleep(1)
            tasks[task_num] = task_to_add

        elif choice == 2:

            print(tasks)

            select_delition = int(input("select the number of the task you want to delete: "))

            del tasks[select_delition]

            print(tasks)

        elif choice ==3:
            print(tasks)

        elif choice == 4:

            for key , value in tasks.items():
                to_do_file.write(f"{key} :{value}")
                to_do_file.write("\n")
                app_in_use = False

        else:
            print("input not valid sorry")




