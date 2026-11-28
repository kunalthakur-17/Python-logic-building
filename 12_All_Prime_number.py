# Check Prime Number 

nums = 17

if nums <= 1:
    print("Not Prime")
else:
    for i in range(2, nums):
        if nums % i !=0:
            print(i)
    