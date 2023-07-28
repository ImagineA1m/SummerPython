import random
import time
# Project one: What am I game
# Wow factor, add in additional use of function on this code
# Basic function
# Your code should welcome the user then,
# run to randomize the datatype of the varible x
# Then print out the varible and allow the user to guess
# then varify if the guess is correct
# This can be accomplished in a few ways but I will outline one path

def grabuser():
    global user
    user = input("Hi, whats your name : ")
    if len(user) > 0:
        main()        
    else:
        print("please add your name")
        user = input("Hi, whats your name : ")
        main()

def main():
    global x
    global userinput
    userinput = int(input("Type in a whole number. This is going to be the X variable : "))
    x = userinput
    num = [0,1,2]
    num = random.choice(num)
    if num == 0:
        StoI()
    elif num == 1:
        StoB()
    elif num == 2:
        StoA()
    elif num == 3:
        ItoS()
    elif num == 4:
        ItoB()
    elif num == 5:
        ItoA()
    elif num == 6:
        BtoS()
    elif num == 7:
        BtoA()
    elif num == 8:
        BtoI()
    elif num == 9:
        AtoS()
    elif num == 10:
        AtoI()
    elif num == 11:
        AtoB()

# print out explaination of the rules
# get 100(or as many as you want to test) random numbers that range from 0-11
# Assign each function a number and run that function when that number is chosen
# after all the functions run print x
# ask user what datatype they think x is

# for all functions if x does not already exist create x so that you can return x
# if x does not exist then return (datatype) x
# repeated in each function


def StoI():

    if 'x' in globals():
        print("It landed on 0️⃣")
        converted_num = int(x)
        print("X =", converted_num)

        answer = input("What datatype do you think it is ? : \n 1 = int \n 2 = string \n 3 = bool \n 4 = array \n Your Answer : ")
                                                                                                              
        while answer == "":
            answer = input("Your Answer : ")
        if answer == "1":
            print("✅ You Got It! ")
            LoopMain = input("Want to try again? 🤔: ")
            if LoopMain == "yes":
                main()
            else:
                exit()
        else:
            print("❌ You're wrong " + user + " it was a int")
            LoopMain = input("Want to try again? 🤔: ")
            if LoopMain == "yes":
                main()
            else:
                exit()
    else:
        print("the x doesn't exist \n The game will end ❌")


    # this is the string to int function
    # check if the parameter x already exists
    # check if x is a string
    # if both are true then convert the type to interger and return it
    # if either is not true exit the function
    pass


def StoB():
    if 'x' in globals():
        print("It landed on 1️⃣")
        # converted_bool = bool(x)
        # print("X =", converted_bool)
        x = [True] * userinput
        BoolSum = sum(x)
        print(BoolSum)
        answer = input("What datatype do you think it is ? : \n 1 = int \n 2 = string \n 3 = bool \n 4 = array \n Your Answer : ")
                                                                                                              
        while answer == "":
            answer = input("Your Answer : ")
        if answer == "3":
            print("✅ You Got It! ")
            LoopMain = input("Want to try again? 🤔: ")
            if LoopMain == "yes":
                main()
            else:
                exit()
        else:
            print("❌ You're wrong " + user + " it was a bool")
            LoopMain = input("Want to try again? 🤔: ")
            if LoopMain == "yes":
                main()
            else:
                exit()
    else:
        print("the x doesn't exist \n The game will end ❌")

    # this is the string to bool function
    # check if the parameter x already exists
    # check if x is a string
    # if both are true then convert the type to bool and return it
    # if either is not true exit the function
    pass


def StoA():

    if 'x' in globals():
        print("It landed on 2️⃣")
        print(xe)
        answer = input("What date type do you think it is? : \n 1 = int \n 2 = string \n 3 = bool \n 4 = array \n Your Answer :")

        while answer == "":
            answer = input("Your Answer : ")
        if answer == "4":
            print("✅ You Got It! ")
            LoopMain = input("Want to try again? 🤔: ")
            if LoopMain == "yes":
                main()
            else:
                exit()
        else:
            print("❌ You're wrong " + user + " it was a list/array")
            LoopMain = input("Want to try again? 🤔: ")
            if LoopMain == "yes":
                main()
            else:
                exit()
    else:
        print("the x doesn't exist \n The game will end ❌")

        
        
        array = [x]
        print(array)
        
        if isinstance(x, list):
            print("yes")
        else:
            ("no")
        

    #     answer = input("What datatype do you think it is ? : \n 1 = int \n 2 = string \n 3 = bool \n 4 = array \n Your Answer : ")
                                                                                                              
    #     while answer == "":
    #         answer = input("Your Answer : ")
    #     if answer == "4":
    #         print("✅ You Got It! ")
    #         LoopMain = input("Want to try again? 🤔: ")
    #         if LoopMain == "yes":
    #             main()
    #         else:
    #             exit()
    #     else:
    #         print("❌ You're wrong " + user + " it was a array")
    #         LoopMain = input("Want to try again? 🤔: ")
    #         if LoopMain == "yes":
    #             main()
    #         else:
    #             exit()
    # else:
    #     print("the x doesn't exist \n The game will end ❌")
    # this is the string to array function
    # check if the parameter x already exists
    # check if x is a string
    # if both are true then convert the type to array and return it
    # if either is not true exit the function


def ItoS():
    print("It landed on 3️⃣")



    # this is the int to string function
    # check if the parameter x already exists
    # check if x is a int
    # if both are true then convert the type to string and return it
    # if either is not true exit the function
    pass


def ItoB():
    print("It landed on 4️⃣")
    # this is the int to bool function
    # check if the parameter x already exists
    # check if x is a int
    # if both are true then convert the type to bool and return it
    # if either is not true exit the function
    pass


def ItoA():
    print("It landed on 5️⃣")
    # this is the int to string function
    # check if the parameter x already exists
    # check if x is a int
    # if both are true then convert the type to array and return it
    # if either is not true exit the function
    pass


def BtoS():
    print("It landed on 6️⃣")
    # this is the bool to string function
    # check if the parameter x already exists
    # check if x is a bool
    # if both are true then convert the type to string and return it
    # if either is not true exit the function
    pass


def BtoA():
    print("It landed on 7️⃣")
    # this is the bool to array function
    # check if the parameter x already exists
    # check if x is a bool
    # if both are true then convert the type to array and return it
    # if either is not true exit the function
    pass


def BtoI():
    print("It landed on 8️⃣")
    # this is the bool to interger function
    # check if the parameter x already exists
    # check if x is a bool
    # if both are true then convert the type to string and return it
    # if either is not true exit the function
    pass


def AtoS():
    print("It landed on 9️⃣")
    # this is the array to string function
    # check if the parameter x already exists
    # check if x is a array
    # if both are true then convert the type to string and return it
    # if either is not true exit the function
    pass


def AtoI():
    print("It landed on 🔟")
    # this is the array to int function
    # check if the parameter x already exists
    # check if x is a array
    # if both are true then convert the type to int and return it
    # if either is not true exit the function
    pass


def AtoB():
    print("It landed on 1️⃣1️⃣")
    # this is the array to bool function
    # check if the parameter x already exists
    # check if x is a array
    # if both are true then convert the type to bool and return it
    # if either is not true exit the function
    pass
# challenges when complete with first part
# add a counter on the functions to count how many times the datatype was
# converted successfully. So only if x exists and is whatever type it needs
# to be, increment that counters value by one
# Let the user choose how many random numbers are generated
# make a for or while loop to let the user play multiple times
# look at your code and see what lines are repeated over and over
# can a new function be made to solve this?
# advanced counter, now count how many times x was each datatype]


grabuser()
