import datetime
from tabulate import tabulate
from colorama import Fore, Style, init

# Activate the colorama library
init(autoreset=True)

def display_welcome_message():
    """Display the welcome message and options menu."""
    print(Fore.GREEN + "\n** Welcome to the Task Manager program from Almadrsa **")
    print(tabulate([["1. Add a task"], ["2. Delete a task"], ["3. Display tasks"], ["4. Exit"]], tablefmt="fancy_grid"))

def get_current_datetime():
    """Get the current date and time."""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")

def add_task(tasks):
    """Add a task to the tasks list."""
    while True:
        task_name = input(Fore.GREEN + "\n** Enter the task name: ").strip()
        task_date, task_time = get_current_datetime()
        tasks.append({"Task Name": task_name, "Date": task_date, "Time": task_time})
        print(Fore.GREEN + f"** Task '{task_name}' added successfully on {task_date} at {task_time} **\n")

        response = input("** Do you want to add another task? (y/n): ").strip().lower()
        while response not in ["y", "n"]:
            print(Fore.RED + "** Please enter 'y' or 'n' **")
            response = input("** Do you want to add another task? (y/n): ").strip().lower()

        if response == "n":
            break

def delete_task(tasks):
    """Delete a task from the tasks list."""
    task_name_to_delete = input(Fore.RED + "\n** Enter the task name you want to delete: ").strip()
    found_task = find_task_by_name(tasks, task_name_to_delete)

    if found_task:
        confirm_delete = input(Fore.RED + f"\n** Are you sure you want to delete the task '{task_name_to_delete}'? (y/n): ").strip().lower()
        while confirm_delete not in ["y", "n"]:
            print(Fore.RED + "** Please enter 'y' or 'n' **")
            confirm_delete = input(Fore.RED + f"** Are you sure you want to delete the task '{task_name_to_delete}'? (y/n): ").strip().lower()

        if confirm_delete == "y":
            tasks.remove(found_task)
            print(Fore.GREEN + f"** Task '{task_name_to_delete}' deleted successfully. **\n")
        else:
            print(Fore.RED + "** Deletion of the task has been canceled. **")
    else:
        print(Fore.RED + f"** The task '{task_name_to_delete}' is not found in the task list. **\n")

def find_task_by_name(tasks, task_name):
    """Find a task in the tasks list by name."""
    for task in tasks:
        if task["Task Name"] == task_name:
            return task
    return None

def display_tasks(tasks):
    """Display all tasks in a formatted table."""
    if not tasks:
        print(Fore.RED + "\n** No tasks in the list. **\n")
        return

    headers = ["Task Name", "Date", "Time"]
    data = [[task["Task Name"], task["Date"], task["Time"]] for task in tasks]

    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
    print()

def main():
    """Main function to run the Task Manager program."""
    tasks_list = []

    while True:
        display_welcome_message()
        choice = input("** Enter the number of the action you want to perform (1/2/3/4): ").strip()

        if choice == "1":
            add_task(tasks_list)
        elif choice == "2":
            delete_task(tasks_list)
        elif choice == "3":
            display_tasks(tasks_list)
        elif choice == "4":
            print("\n** Exiting the Task Manager program. Goodbye! **\n")
            break
        else:
            print(Fore.RED + "** Invalid input. Please enter a valid number. **\n")

        another_action = input("** Do you want to perform another action? (y/n): ").strip().lower()
        while another_action not in ["y", "n"]:
            print(Fore.RED + "** Please enter 'y' or 'n' **")
            another_action = input("** Do you want to perform another action? (y/n): ").strip().lower()

        if another_action == "n":
            break

if __name__ == "__main__":
    main()
