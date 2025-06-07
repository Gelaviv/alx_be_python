def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        # Prompt for and add an item
        if choice == '1':
            add_to_list = input("Enter the item to add:").lower()            
            if add_to_list:
                shopping_list.append(add_to_list)
                print(f"'{add_to_list}' has been added to your shopping list.")
            else:
                print("No item entered. Please try again.")
            pass
        elif choice == '2':
            # Prompt for and remove an item
            remove_from_list = input("What is the name of the item to be removed?").lower()
            if remove_from_list in shopping_list:
                shopping_list.remove(remove_from_list)
                print(f"'{remove_from_list}' has been removed from your shopping list.")
            else:
                print(f"'{remove_from_list}' was not found in your shopping list.")

            pass
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("Your shopping list is empty")
                
            else:
                for list in shopping_list:
                    print(list)

            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()