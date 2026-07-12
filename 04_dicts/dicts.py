# Dictionaries in Python

# Creating a dict
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

# Accessing values
print(chai_types["Masala"])         # Spicy
print(chai_types.get("Ginger"))     # Zesty
print(chai_types.get("Pink"))       # None — no error if key doesn't exist

# Looping — keys only
for chai in chai_types:
    print(chai)

# Looping — keys and values
for chai in chai_types:
    print(chai, chai_types[chai])

# Looping with .items()
for key, value in chai_types.items():
    print(key, value)

# Checking if a key exists
if "Masala" in chai_types:
    print("I have masala chai")

# Adding a new key
chai_types["Earl Grey"] = "citrus"

# Removing items
chai_types.pop("Ginger")       # remove by key
chai_types.popitem()           # remove last inserted item
del chai_types["Green"]        # delete by key

# Copying a dict
chai_types_copy = chai_types.copy()

# Nested dict
tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "Tea": {"Green": "Mild", "Black": "Strong"}
}

print(tea_shop["chai"])              # {'Masala': 'Spicy', 'Ginger': 'Zesty'}
print(tea_shop["chai"]["Ginger"])    # Zesty

# Dict comprehension
squared_num = {x: x**2 for x in range(6)}
print(squared_num)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Clearing a dict
squared_num.clear()
print(squared_num)   # {}

# dict.fromkeys() — create dict from a list with a default value
keys = ["Masala", "Ginger", "Lemon"]
new_dict = dict.fromkeys(keys, "Delicious")
print(new_dict)   # {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
