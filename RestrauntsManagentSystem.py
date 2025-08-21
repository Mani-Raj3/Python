# Define the menu of restraunt

menu = {
    'pizza':40,
    'pasta':50,
    'Burger':60,
     'Salad':70,
     'Coffee':80,

}

# Greet --.. Welcome krne ke liye

print("Wlcome to PYTHON Restraunt")

print("Pizza: Rs 40\nPasta: Rs 50\nBurger: Rs 60\nSalad: Rs 70\nCoffee: Rs 90")

order_total = 0
# 80 + 70 = 150

item_1 = input("Enter the name of item you want to order = ")

if item_1 in menu:
    order_total += menu[item_1]  # 0+50
    print(f"Your item {item_1} has been added to your oreder")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No)")

if another_order =="Yes":
    item_2 = input("Enter the namse of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]

        print(f"Item {item_2} has been addes to order")
    else:
        print(f"Ordered item { item_2} is not available! ")

print(f"the total amount of items is to pay {order_total}")        