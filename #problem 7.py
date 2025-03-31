#problem 7
def dispense_cash(amount):
    if amount % 500 != 0:
        print("Invalid amount! Enter a multiple of ₹500.")
        return
    
    notes_2000 = amount // 2000 
    remaining = amount % 2000    

    notes_500 = remaining // 500  

    print("₹2000 notes: ",notes_2000)
    print("₹500 notes: ",notes_500)

amount = int(input("Enter the amount: "))
dispense_cash(amount)

