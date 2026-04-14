import time

file_path = r"/home/gryphon_/Todo/TO_DO.txt" #file can change if working from home :] 

with open (file_path,"w") as to_do_file:

    app_in_use = True

    
    task_num = 0
    tasks = {}

    

    while app_in_use:

        print('Welcome to to do app')
        print('1 to add , 2 to remove , 3 to see tasklist , 4 to complete the tasklist')
        time.sleep(1)
        choice = int(input("What would you like to do: "))

        if choice == 1:
            task_num +=1
            task_to_add = input ("add your task: ") #example -> Do the dishes




