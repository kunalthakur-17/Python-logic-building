# Multiplication Table

table = int(input("Enter a number: "))
lengthOfTable = int(input("Enter a number: "))

def Multiplication_Table(table,lengthOfTable):
    for start in range(1,lengthOfTable+1):
        print(f"{table} X {start} = {table*start}")


Multiplication_Table(table,lengthOfTable)