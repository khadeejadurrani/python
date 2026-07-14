#Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89),
#  C (70-79), D (60-69), F (below 60).

grade_string = input ("enter student marks: ")
grade = float(grade_string)

if(grade>=90 and grade<=100) :
    print("grade : A")
elif(grade>=80 and grade<=89):
    print("grade : B")
elif(grade>=70 and grade<=79):
    print("grade : C")
elif(grade>=60 and grade<=69):
    print("grade : D")
elif(grade < 60):
    print("grade : F")
else:
    print ("enter number between 0-100")
