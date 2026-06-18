print(" CONTACT BOOK")
print("1. Add Contact")
print("2. View Contacts")
print("3. Search Contact")
print("4. Update Contact")
print("5. Delete Contact")

choice = eval(input("\nEnter choice number (1-5): "))

if choice == 1:
    print("You selected: Add Contact")
    
elif choice == 2:
    print("You selected: View Contacts")
    
elif choice == 3:
    print("You selected: Search Contact")
    
elif choice == 4:
    print("You selected: Update Contact")
    
elif choice == 5:
    print("You selected: Delete Contact")
    
else:
    print("Invalid choice!")