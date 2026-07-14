#Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk,
#  Rainy - Read a book, Snowy - Build a snowman).

weather = input("enter weather : ")

if(weather=="sunny"): 
    print("lets go for a walk")
elif(weather=="rainy"):
    print("read a book")
elif(weather=="snowy"):
    print("fruit is ripe")
else:
    print("enter only the weathers - Sunny , Rainy , Snowy")