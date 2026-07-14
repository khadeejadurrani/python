#10. Pet Food Recommendation
#Problem: Recommend a type of pet food based on the pet's species and age. 
# (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = input("enter your pet specie(dog , cat , rabbit , bird) and age (ex:cat 3)")

#here we declared two variables together and then we split up the input and stoed them
#in two different variables , .split() splits the input where there is a space
specie , age_str = pet.split()

# age is still in form of string so we convert it to number
age = float(age_str)

if(specie == "dog"):
    if(age<1):
        print("it is a puppy , food : puppy food")
    elif(age<= 7):
        print("it is a adult , food : adult dog food")
    else:
        print("it is a senior , food : senior dog food")
elif(specie == "cat"):
    if(age<1):
        print("it is a kitten , food : kitten food")
    elif(age<= 7):
        print("it is a  adult, food : adult cat food")
    else:
        print("it is a senior , food : senior cat food")

elif(specie == "bird"):
    if(age< 0.5):
        print("it is a Chick/juvenile , food : Hand-feeding formula / soft food")
    else:
        print("it is a adult , food : Adult seed/pellet mix")

elif(specie == "rabbit"):
    if(age < 0.7):
        print("it is a young rabbit , food : Alfalfa-based food (higher protein)")
    else:
        print("it is a adult rabbit , food : Timothy-hay-based food (lower calcium)")

else:
    print("enter only the pets : cat , dog , bird , rabbit and age in months(make it in points)")