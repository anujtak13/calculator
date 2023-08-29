#2calcu
print("what you want to do:-")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
addop = int(input())
# subtr = int(input("2 for subtraction"))
# multipl = int(input("3 for multiplication"))
# divis = int(input("4 for division"))
if addop > 4:
    print("select proper no5")
    exit()
a = int(input("write your value:"))
b = int(input("second value:"))

class addition:
    def __init__(self):
       add = (float(a + b))
       print(add)
# additi
# on()
class subtraction:
    def __init__(self):
        sub = (int(a - b))
        print(sub)
# subtraction()
class division:
    def __init__(self):
        if b > a:
            print("denominator cant be less than numerator")
        else:
            div = (float(a / b))
            print(div)
# division()

class multiplication:
    def __init__(self):
        if a&b == 0:
            print(" 0 can't multiply by any number")
        else:
            multi = (float(a * b))
            print(multi)
# multiplication()

if addop == 1:
    print("you select addition operation")
    addition()
elif addop == 2:
    print("you select for subtraction")
    subtraction()
elif addop == 3:
    print("you select for multiplication")
    multiplication()
elif addop == 4:
    print("you select for divison")
    division()

else:
    print("select proper number of operation")
