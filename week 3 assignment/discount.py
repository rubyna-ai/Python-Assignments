amount = float(input("Enter total purchase amount:"))
member = ("Are you a loyalty member? (Yes/No):")

if amount<1000:
    discount= 0;
elif amount<4999:
    discount= 0.05;
elif amount<14999:
    discount= 0.10;
else: 
    discount = 0.20;
