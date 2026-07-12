# Lists in Python

# Creating a list
teas = ["lemon tea", "ginger tea", "masala chai"]
mixed = [1, "chai", 3.14, True]
nested = [1, [2, "three"], 4, 5]

# Indexing and slicing
print(teas[0])      # lemon tea
print(teas[-1])     # masala chai
print(teas[0:2])    # ['lemon tea', 'ginger tea']

# Lists are mutable — can be changed in place
teas[0] = "mint tea"
print(teas)

# Common list methods
teas.append("noon chai")         # add to end
teas.insert(1, "kashmiri chai")  # add at index
teas.remove("mint tea")          # remove by value
popped = teas.pop()              # remove and return last item
print(popped)

# Useful operations
nums = [3, 1, 4, 1, 5, 9]
print(len(nums))        # 6
print(sorted(nums))     # [1, 1, 3, 4, 5, 9]
print(sum(nums))        # 23
print(min(nums))        # 1
print(max(nums))        # 9

# Checking membership
print("noon chai" in teas)   # True/False

# Looping through a list
for tea in teas:
    print(tea)

# List comprehension
squares = [x**2 for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]
