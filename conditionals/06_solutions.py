#Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk,
# 3-15 km: Bike, >15 km: Car).

while True:
    distance_input = input("enter distancde you want to travel: ")
    if (type(distance_input) == 'int' or type(distance_input) == 'float'):
        distance = float(distance_input)

        if(distance < 3): 
            print("choose walk")
        elif(distance <= 15):
            print("chose bike")
        else:
            print("choose car")

    else:
        print("enter only numbers for distance")


    again = input("want to put another number (y/n): ")
    if again.lower() != "y":

        break 

