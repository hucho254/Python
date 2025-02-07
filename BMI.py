Weight=float(input("Enter your weight: "))
Height=float(input("Enter your height: "))

BMI=Weight/(Height*Height)
if BMI<18.5:
    classification='underweight'
elif BMI>18.5 and BMI<25:
    classification='normal'
elif BMI>25 and BMI<30:
    classification='overweight'
else:
    classification='obese'
print(f"your BMI is {BMI:.2f}, which is considered {classification}")
