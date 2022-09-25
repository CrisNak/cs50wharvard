import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError: #se no lugar de um numero foir colocado uma palavra ou letra
    print("error: invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("error: Cannot divide by 0.")
    sys.exit(1)
    #se a equação for dividida por 0, sai do programa

print(f"{x} / {y} = {result}")