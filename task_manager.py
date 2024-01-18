# Capstone Project: Modified a program that manages tasks assigned to each member of a team for a small business.
#Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create task.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file: #modified to a to avoid data being overwritten
        pass
    
with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)
    
def reg_user():
    
    try:
        new_username = input("New Username: ")
        if new_username in username_password:
            print("Username already exists:  ",new_username, menu)
                           
    except ValueError:
        print("Error, please try again: ")
            
    new_password = input("New Password: ")
    confirm_password = input("Confirm Password: ")
    if new_password == confirm_password:
        print("New user added")
        username_password[new_username] = new_password
        
        with open ('user.txt', 'w') as user_file: #modified to out_file to user file
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            user_file.write("\n".join(user_data))
            #user_file.write(f"\n{new_username} ; {new_password}") #added newline space before each entry    
                
    else:
        print("Passwords do no match")
                                       
    
def add_task():
    
    task_username = input("Name of person assigned to task: ")
    with open ("user.txt", "r") as user_file: #opens and reads user file to check usernames
            if task_username not in username_password.keys(): 
                print("User does not exist. Please enter a valid username") #removed line to continue
               
           
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")


def view_all(task_file):
    
    with open('tasks.txt', 'r') as task_file:
        content = task_file.read()
        task_data = content.split('\n')
                
    task_list = [] #used within function to append dictionary
    for task_string in task_data:
        if task_string:
            task_components = task_string.split(';') #splits data into a dictionary
            current_tasks = {
                'username' :  task_components[0],
                'title' : task_components[1],
                'description' : task_components[2],
                'due_date' : datetime.strptime(task_components[3], DATETIME_STRING_FORMAT),
                'assigned_date' : datetime.strptime(task_components[4], DATETIME_STRING_FORMAT),
                'completed' : True if task_components[5] == "Yes" else False
            }
            task_list.append(current_tasks)
            
    with open ('tasks.txt', 'r') as task_file:#re-opened file
                                        
        for t in task_list: #used to print tasks
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: {t['description']}\n"
            print(disp_str)
                 

def view_mine():
    
    for i, t in enumerate (task_list, 1): #task index starts at 1
            if current_user == t["username"]: 
                disp_str = f"Task : {i} \n" 
                disp_str += f"Title: \t\t {t['title']}\n"
                disp_str += f"Assigned to: \t {t['username']}\n"
                disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {t['due_date'] < datetime.today()}\n"
                disp_str += f"Task Description: {t['description']}\n"
                print(disp_str) 
                
    while True:
        try:
            task_number = int(input("Please enter a task number: ")) 
            if task_number >= 0 and task_number <= len(task_list):
                task_index = task_number -1
                break
        except ValueError:
                print("Invalid task number, please try again: ") 
        
    if task_number == -1: 
        task_number == menu 
                                                 
    print("""Please select from one of the following options or -1 to return to main menu:
                1. Mark task as complete
                2. Edit task
            """)
        
    option = input("Please enter 1 or 2 for the options above: ")
                        
    if option == '1':
        chosen_task = task_list[task_index]
        if chosen_task['completed'] == False:
            chosen_task['completed'] = True
            task_list[task_index] = chosen_task
            print("Task completed")
                
                                                    
    elif option == '2':
        chosen_task = task_list[task_index]
        if chosen_task['completed'] == True:
            print("This task is completed and cannot be edited")
                
        elif chosen_task['completed'] == False:
            edit_username = input("Please enter new_username: ")
            chosen_task['username'] = edit_username
            task_list[task_index] = chosen_task
            print("The assigned username has been changed.")
            
        if edit_username not in username_password.keys():
            print("Username does not exist. Please enter a valid username")
        
        while True:
            try:
                if chosen_task['completed'] == True:
                    print("This task is completed and cannot be edited")
                
                elif chosen_task['completed'] == False:
                    edit_due_date =input("Please enter the new due date (YYYY-MM-DD): ")
                    chosen_task['due_date'] = datetime.strptime(edit_due_date, DATETIME_STRING_FORMAT)
                    task_list[task_index] = chosen_task
                    print("The task due date has been edited")
                break
            except ValueError:
                print("You have entered invalid date format, please enter (YYYY-MM-DD)")


#====Login Section====
# '''This code reads usernames and password from the user.txt file to allow a user to login.'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split('\n')

# Convert to a dictionary
username_password = {}
try:#added try/except to handle value error
    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password
except:ValueError
    
logged_in = False
while not logged_in:

    print("LOGIN")
    current_user = input("Username: ")
    current_pass = input("Password: ")
    if current_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[current_user] != current_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True
          
                 
while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View and edit my tasks
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        
        '''Add a new user to the user.txt file'''
        # - Request input of a new username and new password
        
        reg_user()    
                
    elif menu == 'a':
        
        add_task()
       
                                  
    elif menu == 'va':
        
        '''Reads the task from tasks.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''
        view_all(task_file)
            
                     
    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''     
        
        view_mine()
       
                                                                          
    elif menu == 'gr':
        
                   
        task_overview = "task_overview.txt"
        user_overview = "user_overview.txt"
        
        with open("tasks.txt", 'r') as task_file:
            task_data = task_file.read().split("\n")
            task_data = [t for t in task_data if t != ""]

        task_list = []
        for t_str in task_data:
            curr_t = {}

            # Split by semicolon and manually add each component
            task_components = t_str.split(";")
            curr_t['username'] = task_components[0]
            curr_t['title'] = task_components[1]
            curr_t['description'] = task_components[2]
            curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
            curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
            curr_t['completed'] = True if task_components[5] == "Yes" else False

            task_list.append(curr_t)
                
            total_num_tasks = len(task_list)
            total_completed_tasks = sum(t ['completed'] for t in task_list)
            total_uncompleted_tasks = sum(not t ['completed'] for t in task_list)
            total_overdue_tasks = sum(1 for t in task_list if t['due_date'] < datetime.today())
            percentage_uncompleted_tasks = (total_uncompleted_tasks / total_num_tasks) * 100 if total_num_tasks > 0 else 0
            percentage_overdue_tasks = (total_overdue_tasks / total_num_tasks) * 100 if total_num_tasks > 0 else 0
            total_num_users = len(username_password.keys())
                
            with open ('task.overview.txt', 'w') as new_task_file: #creates and writes to task overview text file
                new_task_file.write(f"Tasks overview: \n\n")
                new_task_file.write(f"Total number of tasks : {total_num_tasks}\n")
                new_task_file.write(f"Total completed tasks : {total_completed_tasks}\n")
                new_task_file.write(f"Total uncompleted tasks : {total_uncompleted_tasks}\n")
                new_task_file.write(f"Total overdue tasks : {total_overdue_tasks}\n")
                new_task_file.write(f"Percentage of overdue tasks : {int(percentage_overdue_tasks)}%\n")
            
            with open ('user_overview.txt', 'w') as new_user_file: #creates and writes to user overview text file       
                new_user_file.write(f"User overview: \n\n")
                new_user_file.write(f"Total number of users = {total_num_users}\n")
                
                for username in username_password.keys():
                    assigned_tasks = sum(1 for t in task_list if t['username'] == username)
                    user_completed_tasks = sum(1 for t in task_list if t['username'] == username and t['completed'] == True)
                    user_uncompleted_tasks = sum(1 for t in task_list if t ['username'] == username and t ['completed'] == False)
                    user_overdue_tasks = sum(1 for t in task_list if t['username'] == username and t['due_date'] < datetime.today()) 
                    percentage_assigned_tasks = (assigned_tasks / total_num_tasks) * 100 if total_num_tasks > 0 else 0
                    percentage_user_completed_tasks = (user_completed_tasks / assigned_tasks) * 100 if assigned_tasks > 0 else 0
                    percentage_user_overdue_tasks = (user_overdue_tasks / assigned_tasks) * 100 if assigned_tasks > 0 else 0
                    
                    new_user_file.write(f"\nUser: {username}\n")
                    new_user_file.write(f"Assigned tasks: {assigned_tasks}\n")
                    new_user_file.write(f"Completed tasks: {user_completed_tasks}\n")
                    new_user_file.write(f"Uncompleted tasks: {user_uncompleted_tasks}\n")
                    new_user_file.write(f"Overdue tasks: {user_overdue_tasks}\n")
                    new_user_file.write(f"Percentage of assigned tasks: {int(percentage_assigned_tasks)}%\n")
                    new_user_file.write(f"Percentage of completed tasks: {int(percentage_user_completed_tasks)}%\n")
                    new_user_file.write(f"Percentage overdue tasks = {int(percentage_user_overdue_tasks)}%\n")
      
    elif menu == 'ds': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        
  
        if current_user == 'admin':
           
            with open ('tasks.txt') as  task_file: #prints from text file
                
                for t in task_list:
                    total_num_tasks = (len(task_list))
                    total_completed_tasks = sum(t ['completed'] for t in task_list)
                    total_uncompleted_tasks = sum( not t ['completed'] for t in task_list)
                    total_overdue_tasks = sum(1 for t in task_list if t['due_date'] < datetime.today())
                    percentage_overdue_tasks = (total_overdue_tasks / total_num_tasks) * 100 if total_num_tasks > 0 else 0
                    total_num_users = (len(username_password.keys()))
                                
                    display_stat =(f"Tasks overview: \n\n")
                    display_stat +=(f"Total number of tasks : {total_num_tasks}\n")
                    display_stat +=(f"Total completed tasks : {total_completed_tasks}\n")
                    display_stat +=(f"Total uncompleted tasks : {total_uncompleted_tasks}\n")
                    display_stat +=(f"Total overdue tasks : {total_overdue_tasks}\n")
                    display_stat +=(f"Percentage of overdue tasks : {int(percentage_overdue_tasks)}%\n")
                    print(display_stat)
            
                for username in username_password.keys():
                    assigned_tasks = sum(1 for t in task_list if t['username'] == username)
                    user_completed_tasks = sum(1 for t in task_list if t['username'] == username and t['completed'])
                    user_uncompleted_tasks = sum(1 for t in task_list if t ['username'] == username and not t ['completed'])
                    user_overdue_tasks = sum(1 for t in task_list if t['username'] == username and t['due_date'] < datetime.today()) 
                    percentage_assigned_tasks = (assigned_tasks / total_num_tasks) * 100 if total_num_tasks > 0 else 0
                    percentage_user_completed_tasks = (user_completed_tasks / assigned_tasks) * 100 if assigned_tasks > 0 else 0
                    percentage_user_overdue_tasks = (user_overdue_tasks / assigned_tasks) * 100 if assigned_tasks > 1 else 0
                    
                    display_stat =(f"User: {username}\n")
                    display_stat += (f"Assigned tasks: {assigned_tasks}\n")
                    display_stat +=(f"Completed tasks: {user_completed_tasks}\n")
                    display_stat +=(f"Uncompleted tasks: {user_uncompleted_tasks}\n")
                    display_stat +=(f"Overdue tasks: {user_overdue_tasks}\n")
                    display_stat +=(f"Percentage of assigned tasks: {int(percentage_assigned_tasks)}%\n")
                    display_stat +=(f"Percentage of completed tasks: {int(percentage_user_completed_tasks)}%\n")
                    display_stat +=(f"Percentage overdue tasks = {int(percentage_overdue_tasks)}%\n")

                    print(display_stat)
        
        else:
            print("Sorry, only admin has access to view stats")    
                     
        
    elif menu == 'e':
        
        print('Goodbye!!!')
     
        with open('tasks.txt', 'w') as task_file:
                            
            update_task_list = []
            for t in task_list:
                tasks = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                update_task_list.append(";".join(tasks))
            task_file.write("\n".join(update_task_list))

        break