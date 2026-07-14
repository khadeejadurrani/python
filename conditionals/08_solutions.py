#8. Password Strength Checker
#Problem: Check if a password is "Weak", "Medium", or "Strong". 
# Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("enter your password")
password = len(password)

if(password < 6):
    print("weak password")
elif(password <= 10):
    print("weak password")
else:
    print("strong password")

