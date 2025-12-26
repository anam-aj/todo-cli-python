# To-do List App

A terminal based "To-Do List" program


### Video Demo: https://youtu.be/nQXkEzX55L0


### pip install libraries:

* textwrap
* termcolor
* tabulate


### Description:

Project's root directory contains 4 files namely

* project.py : contains the code of the program
* test_project.py : contains test functions that can be checked with pytest
* requirements.txt : contains information about libraries required
* README.md : Detailed description of project

It is a To-do list program which can be completely run from terminal. It lets user create a 'To-do list' which contains a list of tasks. It also gives users the option to view, add, delete task and also mark task as done. When exiting the program it saves the list using pickle module for persistent usage. Program interface is very easy to use. One can simply use the program by reading only what is being shown on screen. User friendly feedback messages are displayed making it easy for the user to understand the working of program. Feedback messages and instructions are colorized and boxed to make it easy to read.

When program is run it provides the user a menu of choices namely
* 1: View Tasks
* 2: Add Task
* 3: Remove Task
* 4: Mark Task as Done
* 5: Save list and Exit program

and then user is prompted for choice with a descriptive message as given below
* Please enter the option number:

user can then enter the option number and then further, easy to follow,
instructions are displayed on screen.

Main code file "project.py" contains the following classes and functions:

* Class
    * Task
    * ToDoList
* Function
    * main
    * menu
    * fetch_list
    * open_list
    * save_list
    * wrap_text

#### Task:
    Creates a 'Task' object with two attributes namely 'detail' and 'status'. 'detail' contains the description of task and 'status' represent whether task is complete or not.

#### ToDoList:
    Creates a 'ToDoList' object, initialized with an instance variable 'task_list' which is an empty list when instantiated. This 'task_list' is then used to store 'Task' objects. It has methods 'add_task' and 'delete_task' which adds or deletes 'Task' objects from 'task_list'.

#### main:
    Contain the core logic of program. It executes the program using other helper functions. First, it loads or create a 'TodoList' object using 'open_list' function and then it print choices to user using 'menu' function. Next it promts user for choice and then according to the input provided by user carry out the respective operation using corresponding helper function.

#### menu:
    It has the choices for menu options stored as a list. It fetches menu items from list, enumerates them and then generate and print a nicely colored formatted menu to user.

#### fetch_list:
    Takes a 'ToDoList' object as argument, fetch 'Tasks' from it and then generate one string per task containing the task-number, task-detail and task-status. Returns a list containing all tasks as such formatted strings.

#### open_list:
    Check if there is a saved file for 'ToDolist' and load it. If not found instantiate a new 'ToDoList'.

#### save_list:
    Saves the user generated 'ToDoList' for persistant usage. It uses pickle module to save the file for future retrieval.

#### wrap_text:
    Helps other function by formatting text. Takes two arguments 'text' and 'color'.It colorize the supplied text in the given colour and put it in a 'box' for better visibility and readability.


### Acknowledgment:

* #### CS50 Duck
    The duck has been a GREAT help! Saved a lot of time by helping in finding required libraries and helping with syntax usage, thus I could invest my time to focus more on core logic.
