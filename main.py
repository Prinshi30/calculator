First= input('enter frist number :')
operator=input('enter operator (+,-,/,*,%) : ')
second= input('enter second number:')

if operator == "+":
    print(int(First) + int(second))
elif operator == "-":
    print(int(First) * int(second))
elif operator == "*":
    print(int(First)-int(second))
elif operator == "/":
    print(int(First) / int(second))
elif operator == "%":
    print(int(First) % int(second))
else:
    print("invalid operator")
    
