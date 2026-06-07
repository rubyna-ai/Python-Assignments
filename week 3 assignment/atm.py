#   ATM Cash withdrawl
balance = int(input("Enter your account balance:"))
daily_withdrawn = int(input("Enter the total amount withdrawn today:"))
amount = int(input("Enter the amount to withdraw:")) 
#input function has been used to take data from the users. Int= integer(whole number)
if amount % 500 != 0: # %modulus operator 
    print("Invalid amount. Amount must be a multiple of NRP 500.")
elif amount>balance: #elif= else if, is used as the case has multiple conditions. Outcome is more than two  
     print("Insufficient balance.")
elif daily_withdrawn + amount > 50000:
    print("Daily limit reached.")
else:
    balance = balance - amount
    print("Withdrawl Successful.")
    print("Your current balance after withdrawl: NRP",balance)
