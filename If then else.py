score= float(input("Enter your score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade= "c"
elif score >= 60:
    grade = "D"
elif score >= 40:
    grade = "E"
else:
    grade = "F for failure!!!"
print(f"Your grade is {grade}")
