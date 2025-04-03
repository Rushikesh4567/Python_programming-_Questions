#problem 10

while True:
    print("\nMovie collection menu:")
    print("1. Add movie")
    print("2. Update ratings")
    print("3. Display movie details")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        atm.check_balance()
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
