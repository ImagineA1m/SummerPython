'''
sum = 0
for i in range(10):
    sum = sum + 1

    print(sum)
fnum = 2
lnum = 2
sum = 0

for i in range(2,2):
    sum = sum + i

print (sum)
'''
# string to int (✅)


def StringToInt():
    String = input("type a number : ")
    converted_num = int(String)
    print(converted_num + 20)

# int to string (❌)


def IntToString():
    Number = int(input("type a number this is the int : "))
    NumberToString = str(Number)
    print(NumberToString + '8')


# int to bool(✅)
def IntToBool():
    Thebool = True
    Number = int(input("Number 1 true\nNumber 2 false :  "))
    if Number == 1:
        Thebool = True
    elif Number == 2:
        Thebool = False
    else:
        print("not a valid number")
    print(Thebool)

def Check():
    test = "9"
    test = [x]
    print(test)
        
    if isinstance(test, list):
        print("yes")
    else:
        ("no")

Check()
