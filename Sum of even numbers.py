numbers=[1,2,3,4,5,6,7,8,9]
# initialise sum variables
sum_even=0
# iterrate over each numbers
for number in numbers:
    # checking if number is even
    if number % 2 == 0:
        # adding the even numbers to the sum
        sum_even += number
print("The sum of all even numbers is:",sum_even)