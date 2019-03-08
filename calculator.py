print("Welcome to Calculator")

print("Select one operation to perform")

print("1. Addition")
print("2. Subtration")
print("3. Multiplication")
print("4. Division")

operation = int(input())

if operation == 1:
    print("Enter 2 Numbers:")
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    sum = num1+num2
    print(sum)
elif operation == 2:
    print("Enter 2 Numbers:")
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    sub = num1-num2
    print(sub)
elif operation == 3:
    print("Enter 2 Numbers:")
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    mul = num1*num2
    print(mul)
elif operation == 4:
    print("Enter 2 Numbers:")
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    div = num1/num2
    print(div)
else:
    print("Wrong choice!")
