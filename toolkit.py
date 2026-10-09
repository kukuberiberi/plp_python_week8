# ==========================================
# Personal Mini-Toolkit (Final Project)
# Combines lists, loops, and conditionals.
# ==========================================

# Tool 1: To-Do List Manager (Uses a changing list)
def todo_manager():
    print("\n--- To-Do List Manager ---")
    tasks = ["Buy groceries", "Finish Python assignment"]
    
    while True:
        print(f"\nCurrent Tasks: {tasks}")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Back to main menu")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            new_task = input("Enter the new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Success: '{new_task}' added!")
            else:
                print("Task cannot be empty.")
        elif choice == "2":
            if not tasks:
                print("Your list is already empty!")
                continue
            print("Current tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                rem_idx = int(input("Enter number of task to remove: ")) - 1
                if 0 <= rem_idx < len(tasks):
                    removed = tasks.pop(rem_idx)
                    print(f"Removed: '{removed}'")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

# Tool 2: Number-Guessing Game (Uses loops and conditionals)
def guessing_game():
    print("\n--- Number-Guessing Game ---")
    secret_number = 7
    attempts = 0
    
    print("I'm thinking of a number between 1 and 10. Try to guess it!")
    
    while True:
        try:
            guess = int(input("Enter your guess (or 0 to quit): "))
            if guess == 0:
                print("Exiting game...")
                break
            
            attempts += 1
            if guess == secret_number:
                print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
        except ValueError:
            print("Please enter a valid integer.")

# Tool 3: Tip & Total Calculator (Uses conditionals and math)
def tip_calculator():
    print("\n--- Tip & Total Calculator ---")
    try:
        bill = float(input("Enter the total bill amount ($): "))
        if bill < 0:
            print("Bill amount cannot be negative.")
            return
            
        print("Select service quality:")
        print("1. Good (20% tip)")
        print("2. Fair (15% tip)")
        print("3. Poor (10% tip)")
        
        service = input("Enter choice (1-3): ").strip()
        
        if service == "1":
            tip_percent = 0.20
        elif service == "2":
            tip_percent = 0.15
        elif service == "3":
            tip_percent = 0.10
        else:
            print("Invalid service choice. Defaulting to 15%.")
            tip_percent = 0.15
            
        tip_amount = bill * tip_percent
        total = bill + tip_amount
        
        print(f"\n--- Summary ---")
        print(f"Bill: ${bill:.2f}")
        print(f"Tip:  ${tip_amount:.2f}")
        print(f"Total: ${total:.2f}")
        
    except ValueError:
        print("Please enter a valid monetary amount.")

# Main Menu Loop
def main():
    print("👋 Welcome to your Personal Mini-Toolkit!")
    
    while True:
        print("\n======================================")
        print("       PERSONAL MINI-TOOLKIT")
        print("======================================")
        print("1. To-Do List Manager")
        print("2. Number-Guessing Game")
        print("3. Tip & Total Calculator")
        print("4. Quit")
        print("======================================")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            todo_manager()
        elif choice == "2":
            guessing_game()
        elif choice == "3":
            tip_calculator()
        elif choice == "4":
            print("\nThank you for using Personal Mini-Toolkit. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Please select an option between 1 and 4.")

if __name__ == "__main__":
    main()