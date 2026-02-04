# inventory management

inventory = [["Bisuits", 50], ["Chocolates", 20], ["Cold Drinks", 100]]

inventory[0][1] = 45 
print("Current Inventory Levels:")
for item in inventory:
    print(f"Product: {item[0]} | Stock: {item[1]}")
    
newProductAdd = inventory.append(["Milk", 14])
print("\nInventory after adding new prod.:")
for item in inventory:
    print(f"Product: {item[0]} | Stock: {item[1]}")
    
removeProductAdd = inventory.pop(2)
print("\nInventory after adding new prod.:")
for item in inventory:
    print(f"Product: {item[0]} | Stock: {item[1]}")