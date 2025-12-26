# Program to implement a 'To-Do List' app


import pickle
import textwrap


from termcolor import colored
from tabulate import tabulate


class Task:
    def __init__(self, detail):
        self.detail = detail
        self.status = "Incomplete"

    def __str__(self):
        return self.detail


class ToDoList:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def delete_task(self, task_number):
        task = self.task_list.pop(task_number - 1)
        return task


def main():
    my_list = open_list()

    while True:
        # Display Menu
        menu()

        # Ask user choice
        choice = input(colored("Please enter the option number: ", "yellow"))

        # Display all tasks
        if choice == "1":
            tasks_list = fetch_list(my_list)
            if tasks_list:
                # Tabulate and colorize all tasks
                tabulated_task_list = tabulate(
                    tasks_list, headers=["No.", "Task", "Status"]
                )
                colored_list = colored(tabulated_task_list, "cyan")
                heading = wrap_text("TO DO LIST", "cyan")
                print(f"\n{heading}\n{colored_list}\n")
            else:
                print(wrap_text("To-Do list is Empty\n", "red"))

        # Add Task to the list
        elif choice == "2":
            task = input(colored("Enter Task: ", "cyan"))
            if task:
                task = Task(task)
                my_list.add_task(task)
                print(wrap_text("Task successfully added to list!", "green"))
            else:
                print(wrap_text("Task can not be empty\n", "red"))

        # Remove Task
        elif choice == "3":
            # Ask user for task to be removed
            text = "Please enter below the task-number to be removed\nTaskNumber: "
            task_number = input(colored(text, "cyan"))

            # Remove task and show confirmation
            try:
                integer = int(task_number)
                if integer > 0:
                    deleted_task = my_list.delete_task(integer)
                    print(
                        wrap_text(
                            f"Task '{deleted_task}' has been successfully removed!\n",
                            "green",
                        )
                    )
                else:
                    raise ValueError
            except:
                print(wrap_text("Invalid Task-Number!\n", "red"))

        # Change Task Completion Status
        elif choice == "4":
            # Ask user for task to be marked as complete
            text = "Please enter below the task-number which is complete\nTaskNumber: "
            task_number = input(colored(text, "cyan"))

            # Change completion status
            try:
                integer = int(task_number)
                if integer > 0:
                    completed_task = my_list.task_list[integer - 1]
                    completed_task.status = "Complete"
                    print(
                        wrap_text(
                            f"Task '{completed_task}' has been successfully completed!"
                            "\n",
                            "green",
                        )
                    )
                else:
                    raise ValueError
            except:
                print(wrap_text("Invalid Task-Number!\n", "red"))

        # Save list and Exit
        elif choice == "5":
            save_list(my_list)
            break

        # Invalid input
        else:
            print(wrap_text("Please enter a valid choice", "red"))


def menu():
    """Generate Menu"""

    menu = (
        "View Tasks",
        "Add Task",
        "Remove Task",
        "Mark Task as Done",
        "Save list and Exit program",
    )

    # Display menu items
    print(colored("\nSelect the option number from below", "yellow"))
    for number, option in enumerate(menu):
        print(colored(f"{number + 1}: {option}", "yellow"))
    print()


def fetch_list(list_object):
    """Create table of tasks"""

    tasks = []

    # Fetch tasks from list_object into list
    for number, task in enumerate(list_object.task_list):
        list_item = [number + 1, textwrap.fill(task.detail, width=20), task.status]
        tasks.append(list_item)

    return tasks


def open_list():
    """Load list_object and create it if not found"""

    try:
        with open("todolist.pkl", "rb") as file:
            list_object = pickle.load(file)
    except FileNotFoundError:
        list_object = ToDoList()

    return list_object


def save_list(list_object):
    """Save list object in binary file"""

    with open("todolist.pkl", "wb") as file:
        pickle.dump(list_object, file)


def wrap_text(text, color):
    """Colorize and Decorate text in a Box"""

    # Wrap text
    wrapped_text = textwrap.fill(text, width=20)

    # Split the wrapped text into lines
    lines = wrapped_text.split("\n")

    # Create the top border
    top_border = "+" + "-" * 22 + "+"

    # Create the bottom border
    bottom_border = top_border

    # Add side borders to each line
    boxed_text = [top_border]
    for line in lines:
        boxed_text.append("| " + line.center(20) + " |")
    boxed_text.append(bottom_border)

    # Join the boxed text into a single string
    boxed_text = "\n".join(boxed_text)

    # Colorize text
    colored_text = colored(boxed_text, color)

    return colored_text


if __name__ == "__main__":
    main()
