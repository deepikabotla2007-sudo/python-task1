import copy

def create_inventory():
    return [
        {
            "item": "Laptop",
            "details": {
                "price": 50000,
                "stock": 10,
                "supplier": {"name": "Dell", "rating": 4.5}
            }
        },
        {
            "item": "Phone",
            "details": {
                "price": 20000,
                "stock": 25,
                "supplier": {"name": "Samsung", "rating": 4.2}
            }
        }
    ]



def apply_discount(data, roll_number):
    length = len(data)
    index_to_modify = roll_number % length

    for i in range(len(data)):
        if i == index_to_modify:
            data[i]["details"]["price"] = int(data[i]["details"]["price"] * 0.9)
            data[i]["details"]["stock"] -= 5

    return data



def compare_data(original, modified):
    changed = 0
    unchanged = 0

    for i in range(len(original)):
        if original[i] != modified[i]:
            changed += 1
        else:
            unchanged += 1

    return (changed, unchanged)





roll_number = int(input("Enter your roll number: "))


inventory = create_inventory()


shallow_copy = copy.copy(inventory)
deep_copy = copy.deepcopy(inventory)


shallow_modified = apply_discount(shallow_copy, roll_number)
deep_modified = apply_discount(deep_copy, roll_number)


shallow_result = compare_data(inventory, shallow_modified)
deep_result = compare_data(inventory, deep_modified)


print("\n--- ORIGINAL INVENTORY ---")
print(inventory)

print("\n--- SHALLOW COPY RESULT ---")
print(shallow_modified)

print("\n--- DEEP COPY RESULT ---")
print(deep_modified)

print("\n--- COMPARISON RESULTS ---")
print("Shallow Copy (changed, unchanged):", shallow_result)
print("Deep Copy (changed, unchanged):", deep_result)