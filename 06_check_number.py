# Is a Number Positive Negative or Zero

num = 0

def checkNumber(num):
    if num < 0:
        return "Negative"
    elif num > 0:
        return "Positive"
    else:
        return "Zero"

print(checkNumber(num))