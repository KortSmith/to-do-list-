import sys  # Add this import to use sys.exit()

# display menu options 
def menu_options(t):
    while True:
        print("\nSelect an option:")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Quit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                add_task(t)
            elif choice == 2:
                remove_task(t)
            elif choice == 3:
                view_tasks(t)
            elif choice == 4:
                quit_app(t)
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error has occurred: {e}\n")


print("Welcome to your to-do list app!")

# Add task to list
def add_task(t):
    try:
        chore = input("What task would you like to add: ")
        if chore:
            t[chore] = {}
            print(f"Task '{chore}' added successfully!\n")
        else:
            raise ValueError("Task cannot be completed")
    except ValueError as e:
        print(f"Error: {e}\n")
    except Exception as e:
        print(f"An error has occurred: {e}\n")
    else:
        print("Chore has been added!")

# Remove task from list 
def remove_task(t):
    try:
        chore = input("What task would you like to remove: ")
        if chore in t:
            del t[chore]
            print(f"Task '{chore}' removed successfully!\n")
        else:
            raise KeyError("Task could not be removed")
    except KeyError as e:
        print(f"Error: {e}\n")
    except Exception as e:
        print(f"An error has occurred: {e}\n")
    else: 
        print("Chore has been removed!")

# View all tasks from list
def view_tasks(t):
    try:
        if t:
            print("Current tasks:")
            for task in t:
                print(f"- {task}")
        else:
            print("No tasks available.\n")
    except Exception as e:
        print(f"An error has occurred: {e}\n")


# Quit application
def quit_app(t):
    try:
        quit_choice = input("Would you like to quit the application? (yes/no):")
        if quit_choice.lower() == "yes":
            print("Exiting the application. Goodbye!")
            sys.exit()  # Exits the program
        else:
            print("Continuing with the tasks...\n")
    except Exception as e:
        print(f"An error has occurred: {e}\n")

# Initialize tasks as an empty dictionary
t = {}

# Start the program
menu_options(t)