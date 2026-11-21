# Question: Write a Python program to calculate the sum of two numbers using a function.
# Requirements:
# 1. Take two numbers from the user using input().
# 2. Create a function named sum() that accepts two parameters.
# 3. Add both numbers inside the function.
# 4. Return the result.
# 5. Print the result outside the function.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))

def sum(num1,num2):
    return num1+num2

print(sum(num1,num2))