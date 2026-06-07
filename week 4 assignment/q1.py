# declaring inventory and cart items
inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30},
}

cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12,
}

def process_order(inventory, cart):
    bill = {}
    grand_total = 0

    for item, quantity in cart.items():
        if quantity > inventory[item]["stock"]:
            print(f"Sorry, not enough stock for {item}")
        else:
            price = inventory[item]["price"]
            item_total = price * quantity
            bill[item] = item_total
            grand_total += item_total
            inventory[item]["stock"] -= quantity

    # print bill
    print("---- Bill ----")
    for item, total in bill.items():
        print(f"{item} x{cart[item]} = NPR {total}")
    print(f"Grand Total: NPR {grand_total}")

    # print updated stock
    print("--------------")
    stock_line = ", ".join(f"{item}={details['stock']}" for item in bill for details in [inventory[item]])
    print(f"Updated stock: {stock_line}")

process_order(inventory, cart)
