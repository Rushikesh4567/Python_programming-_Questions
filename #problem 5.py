#problem 5

correct_pin = 1234
attempts = 3

while attempts > 0:
    entered_pin = int(input("Enter your PIN: "))
    
    if entered_pin == correct_pin:
        print("Access granted. Welcome!")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. {attempts} attempts left.")
        
        if attempts == 0:
            print("Card blocked. Please contact your bank.")
