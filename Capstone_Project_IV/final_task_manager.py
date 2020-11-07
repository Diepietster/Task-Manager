# Capstone Project 4
# Final Task Manager

# -- Import the date module, to show the date when a task is created

from datetime import date

today = date.today()

# -- Open the 'user.txt' file as user_file
# -- Set login variable to false as default

is_logged_in = False

with open("user.txt", "r") as user_file:
    while is_logged_in == False:                                                         # -- Flag the while loop
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for line in user_file:
            valid_username, valid_password = line.split(", ")                            # -- Unpack the data in the 'user.txt' file
            if username == valid_username and password == valid_password:
                print("You have logged in!")
                is_logged_in = True                                                      # -- Change the is_logged_in variable to True and can now continue with the rest of the program
                break
            else:
                print("Invalid Credentials...Try again!!!")
        user_file.seek(0)                                                                # -- Set the cursor in the 'user.txt' file back to default

# -- Create a function that can register a new user 

def reg_user():
    while True:
        user_file = open("user.txt", "a")
        new_username = input("Enter a new username: ")
        if new_username == valid_username:                                               # -- Check if the username exists and if true ask again for a NEW username
            print("This username already exists!!!")
            print("Add a NEW username!!!")
        else:
            new_password = input("Enter a new password: ")
            confirm_password = input("Please confirm your password: ")
            if new_password == confirm_password:                                         # -- Check that the passwords are the same and if true continue to add new user
                user_file.write(f"\n{new_username}, {new_password}")
                print("User is registered...")
                break
            else:
                print("Something went wrong...Try Again!!!")
        user_file.close()

# -- Create a function that add tasks to the 'tasks.txt' file

def add_task():
    task_file = open("tasks.txt", "a")
    #task assigned to, task name, description of task, date task assigned, end date, task done
    task_assigned_to = input("Enter the username of which the task is assigned to: ")
    task_name = input("Enter the task name: ")
    task_des = input("Enter a small description of the task: ")
    task_end_date = input("Enter the date of when the task should be done: ")
    task_done = input("Is the task done(yes or no): ")
    task_file.write(f"\n{task_assigned_to}, {task_name}, {task_des}, {today}, {task_end_date}, {task_done}")
    print("Task added successfully...")
    task_file.close()

# -- Create a function that views all the current tasks in the 'tasks.txt' file

def view_all():
    task_file = open("tasks.txt", "r")
    #task assigned to, task name, description of task, date task assigned, end date, task done
    for line in task_file:
        task_assigned_to, task_name, task_des, task_start_date, task_end_date, task_done = line.split(", ")
        print(f"""

        Username: {task_assigned_to}
        Task Name: {task_name}
        Description Of Task: {task_des}
        Date Task Assigned: {task_start_date}
        Date Task Should Be Done: {task_end_date}
        Task Completed: {task_done}
        
        """)
    print("Tasks viewed!")
    task_file.close()

# -- Create a function that shows all the tasks of the username entered in the beginning of the program

def view_mine():
    task_file = open("tasks.txt", "r+")
    counter = 0 
    for line in task_file:                                                                                                                             # -- Iterate through all the users tasks and add a counter to show how many tasks there are
        #task_assigned_to, task_name, task_des, task_start_date, task_end_date, task_done
        task_assigned_to, task_name, task_des, task_start_date, task_end_date, task_done = line.split(", ")
        counter += 1
        if valid_username == task_assigned_to:
            print(f"""

            Tasks Number: {counter}
            Task Name: {task_name}
            Description Of Task: {task_des}
            Date Task Assigned: {task_start_date}
            Date Task Should Be Done: {task_end_date}
            Task Completed: {task_done}
        
            """)
            user_opt = int(input("Enter the task number, if you want to edit that task(if you want to go back to the main menu enter -1): "))
            if user_opt == counter:                                                                                                                    # -- Use if statements to check the user_opt to edit his/her specific tasks                                                                  
                mark_task = input("Is the task done(Yes or No): ")
                task_file.write(f"\n{task_assigned_to}, {task_name}, {task_des}, {task_start_date}, {task_end_date}, {mark_task}")
                if mark_task == "no":
                    edit_task = input("Do you want to edit the username the task is assigned to or the due date(Username or Date): ")
                    if edit_task.lower() == "username":
                        new_task_assigned_to = input("Enter the new name the task is assigned to: ")
                        task_file.write(f"\n{new_task_assigned_to}, {task_name}, {task_des}, {task_start_date}, {task_end_date}, {mark_task}")
                    elif edit_task.lower() == "date":
                        new_end_date = input("Enter the new end date of the task: ")
                        task_file.write(f"\n{new_task_assigned_to}, {task_name}, {task_des}, {task_start_date}, {new_end_date}, {mark_task}")
            elif user_opt == -1:
                print("You have selected to go back to the main menu...")
            else:
                print("Something went wrong!!!")
    print("Viewed my tasks!")
    task_file.close()

# -- Create a function that gives reports from the 'tasks_overview.txt' and user_overview.txt'

def genRep():
    task_over_file = open("tasks_overview.txt", "w")
    task_file = open("tasks.txt", "r")
    due_date = "2020-11-31"
    all_tasks = 0
    done_task = 0
    uncom_task = 0
    exp_task = 0
    for line in task_file:
        line = line.split(", ")
        #task_assigned_to, task_name, task_des, task_start_date, task_end_date, task_done
        all_tasks += 1
        task_done = line(5)
        task_end_date = line(4)
        if task_done == "yes":
            done_task += 1
        else:
            uncom_task += 1
        if task_done == "no" and due_date == task_end_date:
            exp_task += 1
    per_tasks_incom = (uncom_task/all_tasks) * 100
    per_ex_uncom = (exp_task/all_tasks) * 100
    task_over_file.write(f"{all_tasks}, {done_task}, {uncom_task}, {exp_task}, {per_tasks_incom}, {per_ex_uncom}")
    task_over_file.close()
    task_file.close()

    task_file = open("tasks.txt", "r")
    user_over_file = open("user_overview_file.txt", "w")
    total_users_reg = 0
    total_tasks_user = 0
    user_com_task = 0
    tasks_expired = 0
    for line in task_file:
        line = line.split
        task_assigned_to = line(0)
        task_done = line(5)
        total_users_reg += 1
        if username == task_assigned_to:
            total_tasks_user += 1
            if task_done == "yes":
                user_com_task += 1
            else:
                tasks_expired += 1

    per_total_tasks_user = (total_tasks_user/total_users_reg) * 100
    per_com_tasks = (user_com_task/total_tasks_user) * 100
    per_tasks_to_be_done = (user_com_task - tasks_expired/total_tasks_user) * 100
    per_tasks_expired = (tasks_expired/total_tasks_user) * 100

    user_over_file.write(f"{total_users_reg}, {all_tasks}, {total_tasks_user}, {per_total_tasks_user}, {per_com_tasks}, {per_tasks_to_be_done}, {per_tasks_expired}")
    user_over_file.close()

# -- Create a function that shows all the statistics

def dispStats():
    task_over_file = open("tasks_overview.txt", "r")
    for line in task_over_file:
        # -- total_tasks, completed_tasks, uncompleted_tasks, expired_tasks, per_tasks_incom, per_tasks_expired
        total_tasks, completed_tasks, uncompleted_tasks, expired_tasks, per_tasks_incom, per_tasks_expired = line.split(", ")
        print(f"""

        Total number of tasks generated: {total_tasks}
        Total number of comleted tasks: {completed_tasks}
        Total number of uncompleted tasks: {uncompleted_tasks}
        Total number of expired tasks: {expired_tasks}
        Percentage of uncompleted tasks: {per_tasks_incom}%
        Percentage of expired tasks: {per_tasks_expired}%

        """)
    task_over_file.close()

    user_over_file = open("user_overview.txt", "r")
    for line in user_over_file:
        # -- total_users_reg, total_tasks, total_tasks_user, per_total_tasks_user, per_com_tasks, per_tasks_to_be_done, per_ex_uncom
        total_users_reg, total_tasks, total_tasks_user, per_total_tasks_user, per_com_tasks, per_tasks_to_be_done, per_ex_uncom = line.split(", ")
        print(f"""

        Total number of users: {total_users_reg}
        Total tasks: {total_tasks}
        Total tasks specified user: {total_tasks_user}
        Percentage tasks for user out of total tasks: {per_total_tasks_user}%
        Percentage completed tasks: {per_com_tasks}%
        Percentage tasks still to do: {per_tasks_to_be_done}% 
        Percentage tasks expired: {per_ex_uncom}%

        """)
    user_over_file.close()
    print("Statistics Displayed!")

# -- Use a while loop to keep the program going until the user wants to exit the program 

while is_logged_in == True:
    print("""

    R  - Register new user
    A  - Add task
    VA - View all tasks
    VM - View my tasks
    GR - Generate reports
    DS - Display Statistics
    E  - Exit
    
    """)

    user_option = input("Enter what you want to do: ")

    # -- Use if statements to do what the user wants to do, and to call the functions that is needed

    if user_option.lower() == "r":
        print(reg_user())
    elif user_option.lower() == "a":
        print(add_task())
    elif user_option.lower() == "va":
        print(view_all())
    elif user_option.lower() == "vm":
        print(view_mine())
    elif user_option.lower() == "gr":
        print(genRep())
    elif user_option.lower() == "ds":
        print(genRep())
    elif user_option.lower() == "e":
        print("Thank you for using this task manager program, have a nice day!!!")
        break
    else:
        print("Please check user input...Something went wrong!!!")