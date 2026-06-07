accounts = {
    "A001": {"name": "Ramesh Thapa", "balance": 15000, "pin": "1234"},
    "A002": {"name": "Sunita Karki", "balance": 8500,  "pin": "5678"},
    "A003": {"name": "Bikash Rai",   "balance": 22000, "pin": "9012"},
}

def atm(account_id, pin, action, amount=0):

    # checking if account exists
    if account_id not in accounts:
        print("Account not found")
        return

    # getting the account details
    account = accounts[account_id]

    # checking if PIN is correct
    if pin != account["pin"]:
        print("Incorrect PIN")
        return

    # action: checks balance
    if action == "balance":
        print(f"{account['name']} | Balance: NPR {account['balance']}")

    # action: deposit money
    elif action == "deposit":
        account["balance"] += amount
        print(f"Deposited NPR {amount} | New Balance: NPR {account['balance']}")

    # action: withdraw money
    elif action == "withdraw":
        if amount > account["balance"]:
            print("Insufficient funds")
        else:
            account["balance"] -= amount
            print(f"Withdrawn NPR {amount} | New Balance: NPR {account['balance']}")

atm("A001", "1234", "balance")
atm("A002", "0000", "withdraw", 2000)   
atm("A002", "5678", "deposit", 3000)
atm("A003", "9012", "withdraw", 25000)  
atm("A004", "1111", "balance")          
