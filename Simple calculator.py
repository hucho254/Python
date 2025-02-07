num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operator=input("Enter operator:(+,-,*,/,) ")

# perform the calculation based on operator
if operator=="+":
    result=num1+num2
    print(result)
elif operator=="-":
    result=num1-num2
    print(result)
elif operator=="*":
    result=num1*num2
    print(result)
elif operator=="/":
    if num2 != 0:
        result=num1/num2
    else:
        result="Math error"
    print(result) 

