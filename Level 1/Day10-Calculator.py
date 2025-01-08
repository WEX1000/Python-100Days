def add(a, b):
    c = a + b
    return c

def sub(a, b):
    c = a - b
    return c

def multi(a, b):
    c = a * b
    return c

def dev(a, b):
    c = a / b
    return c
while True:
    firstdigit = int(input("What is first number?"))
    seconddigit = int(input("What is second number?"))
    choose = input("What you want to do? + - * /")
    if choose == "+":
        print(f"The answer is: {add(firstdigit, seconddigit)}")
    elif choose == "-":
        print(f"The answer is: {sub(firstdigit, seconddigit)}")
    elif choose == "*":
        print(f"The answer is: {multi(firstdigit, seconddigit)}")
    elif choose == "/":
        print(f"The answer is: {dev(firstdigit, seconddigit)}")
    else:
        print("Wrong choice!")