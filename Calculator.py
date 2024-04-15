#calculator
#Add
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }
should_cont = True
num1 = int(input("first number :"))
while should_cont:
    for symbol in operations:
        print(symbol)
    opt_symbol= input("Pick an symbol from above :")
    calc = operations[opt_symbol]
    num2 = int(input("second number :"))
    cont = input("Do you want to continue 'y' and 'n' to start new calculation :")      
       
    ans = calc(num1, num2)
    print(f"{num1} {opt_symbol} {num2}= {ans}")
    if cont == "y":
        ans = num1
    elif cont == "n":
        should_cont = False
