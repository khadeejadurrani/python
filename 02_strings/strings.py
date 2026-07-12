# Strings in Python

# Creating strings
name = "Khadeeja"
single = 'chai'
multi = """This is a
multi-line string"""

# Strings are immutable — can't change in place
greeting = "hello"
greeting = greeting.upper()  # makes a new string

# Common string methods
print("lemon tea".upper())                           # LEMON TEA
print("CHAI".lower())                                # chai
print("  chai  ".strip())                            # chai
print("chai aur python".replace("chai", "coffee"))   # coffee aur python
print("chai aur python".split(" "))                  # ['chai', 'aur', 'python']

# Indexing and slicing
s = "python"
print(s[0])      # p
print(s[-1])     # n
print(s[0:3])    # pyt
print(s[::-1])   # nohtyp (reversed)

# String formatting
drink = "chai"
temp = 90
print(f"My {drink} is {temp} degrees")

# Checking content
print("chai".startswith("ch"))   # True
print("python".endswith("on"))   # True
print("py" in "python")          # True

# Length
print(len("chai aur python"))    # 15
