#Problem: Movie tickets are priced based on age: $12 for adults (18 and over), 
# $8 for children. Everyone gets a $2 discount on Wednesday

print("welcome to cinema ,please buy your movie ticket please\n $12 for adults ,$8 for children")

ticket_age = input("enter age :")
age = int(ticket_age)

from datetime import datetime

ticket_date = input("enter the date for ticket in format(DD-MM-YYYY) : ")
date_obj = datetime.strptime(ticket_date,"%d-%m-%Y")
day_name = date_obj.strftime("%A")
print(day_name)

if (day_name == "Wednesday") :
    if(age<18):
        print("please pay $6 for ticket \n it is price of child ticket")
    else :
        print("please pay $10 for ticket \n it is price of adult ticket")

else:
    if(age<18):
        print("please pay $8 for ticket \n it is price of child ticket")
    else :
        print("please pay $12 for ticket \n it is price of adult ticket")




