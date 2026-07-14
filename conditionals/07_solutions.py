#7. Coffee Customization
#Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option 
# for "Extra shot" of espresso.

coffee_order = input("enter your coffee order : ")
extra_shot = input("do you wan an extra shot ? (y/n)")

if(coffee_order == "small"): 
    print("small coffee made ")
elif(coffee_order=="medium"):
    print("medium coffee is ready")
elif(coffee_order=="large"):
    print("large coffee is ready")
else:
    print("enter coffee size only")

if(extra_shot=="y"):
    print("extra shot added")
    
