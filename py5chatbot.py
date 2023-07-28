def HasHobbies():
    print('you have hobbies')


def Nohobbies():
    print('you have no hobbies')


def KeepTalking():
    Yesno = input("want to keep chating? : ")
    while Yesno == "yes":
        main()
        if Yesno == "no":
            break


def main():
    global Yesno
    print("Hi my name is Jason")
    hobbies = input("Do you have any hobbies :")
    if hobbies.__contains__("no"):
        Nohobbies()
        KeepTalking()

    else:
        HasHobbies()
        KeepTalking()


main()
