# 1. Grocery Shopping List

grocery_list = ["Milk", "Eggs", "Bread"]
print("grocery list before : ", grocery_list)


addButter = grocery_list.append("Butter")
print("After add butter in list : ", grocery_list)

index_of_eggs = grocery_list.index("Eggs")
print(f"Eggs are at index: {index_of_eggs}")

grocery_list.remove("Milk")
print("after removing milk Final Grocery List:", grocery_list)