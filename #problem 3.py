#problem 3

print("Menu=>\n1.Check Balance\n2.Deposit Money\n3.Withdraw Money\n4.Exit the system")

ch=int(input("Enter your choice from above menu"))
balance=10000
if ch==1:
    print("Your current balance is ",balance)
elif ch==2:
    d=int(input("Enter amount to deposit "))
    balance=balance+d
elif ch==3:
    w=int(input("Enter withdrawal amount "))
    if w>balance:
        print("Invalid input!Please enter valid amount.")
    else:
        balance=balance-w
        printf("The remaining balance is ",balance)
elif ch==4:
    print("Exit")
else:
    print("Invalid choice")