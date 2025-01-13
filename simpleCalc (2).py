

#init

#functions
def add(num1, num2):
    result = num1 + num2
    print(result)

def subtract(num1, num2):
    result = num1 - num2
    print(result)

def multiply(num1, num2):
    result = num1 * num2
    print(result)

def divide(num1, num2):
    result = num1 / num2
    print(result)

def simpleCalculator():
    print("Welcome to simple Calculator")
    print("Please choose an operation")
    print("""1. Add
2. Subtract
3. multiply
4. Divide
5. Quit""")

while True:
    print("Welcome to simple Calculator")


    option = int (input("1-5: "))
    if option  == 1:
        num1 = int(input("Please enter the first number:"))
        num2 = int(input("Please enter the second number:"))
        add(num1,num2)
    elif option == 2:
        num1 = int(input("Please enter the first number:"))
        num2 = int(input("Please enter the second number:"))
        subtract(num1,num2)
    elif option == 3:
        num1 = int(input("Please enter the first number:"))
        num2 = int(input("Please enter the second number:"))
        multiply(num1,num2)
    elif option == 4:
        num1 = int(input("Please enter the first number:"))
        num2 = int(input("Please enter the second number:"))
        divide(num1,num2)

    elif option == 5:
        print("Thank you")

#main
simpleCalculator()

