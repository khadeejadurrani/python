#Problem: Determine if a fruit is ripe, overripe, or unripe based on its color.
#  (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

color = input("enter the color of your fruit : ")

if(color=="Green"): 
    print("fruit is unripe")
elif(color=="Yellow"):
    print("fruit is ripe")
elif(color=="Brown"):
    print("fruit is ripe")
else:
    print("enter only colors : green , yellow , brown")