def main():
    will =int(input("How many marbles : "))
    guess1=int(input("what does jess have : "))
    guess2=int(input("what does tim have : "))
    arr1=[will,jess(will),tim(will)]
    arr2=[will,guess1,guess2]


def jess(will):
    return will + 2
def tim(will):
    return (will + 2) * 2
def arrCheck(arr1,arr2):


# def user():
#     global marbles
#     global will
#     marbles = int(input("How many marbles : "))
#     will = marbles
#     while marbles == "":
#         input("Please enter a valid number of marble")
#     jess()

# def jess():
#     global jes
#     jes = will + 2
#     print(jes)
#     if jes > 0:
#         tim()

# def tim():
#     tim = jes * 2
#     print(tim)

# def guess():

#     will, jes, tim= int(input("How many do they have EX[will,jes,tim]")).split() 
#     if will == will and jes == jes and tim == tim:
#         print("correct")
# user()