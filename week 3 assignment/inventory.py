#inventory restock
inventory = [
    {"item": "Rice", "stock": 5, "threshold": 10},
    {"item": "Eggs", "stock": 24, "threshold": 12},
    {"item": "Milk", "stock": 3, "threshold": 6},
    {"item": "Bread", "stock": 8, "threshold": 5},
    {"item": "Chicken", "stock": 0, "threshold": 4},
    {"item": "Cooking Oil", "stock": 2, "threshold": 3},
]

restockCount= 0;

for i in inventory:
    if(i["stock"]<i["threshold"]):
        print(i["item"], "needs to restock.")
        restockCount+=1
    
    else:
        print(i["item"], "is sufficient");
        
        
print("Total items that needs restocking", restockCount);