


# Question: Write a Python program to calculate the area of a triangle using a function.

# Requirements:
# 1. Take base (b) and height (h) as parameters.
# 2. Create a function named area_of_triangle().
# 3. Calculate the area inside the function.
# 4. Return the result.
# 5. Print the result by calling the function.



b = 10
h = 10

def area_of_triangle(b, h):
    result = 1/2*(b*h)
    return result

print(area_of_triangle(b, h))