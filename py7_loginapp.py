import turtle

#Sign In popup
def done():
    t = turtle.Turtle()
    t.color('Blue')
    style = ('Courier',30,'italic')
    t.write("You have signed in ☑️" + AccountName, font= style, align='center')
    turtle.done()

#make mutiple accounts and loop
#save accounts into arrays

def UsersMulti():
    global AnotherAccountName
    global Username
    global Usernames
    global Password
    global Passwords

    print("You are now creating another user\n")
    AnotherAccountName = input("what should this account name be called? : ")
    Username = input("Username : ")
    Password = input("Password : ")

    print("Now signing in ⬇️")
    UsernameEnter = input("Username : ")
    PasswordEnter = input("Password : ")

    if UsernameEnter == Username and PasswordEnter == Password:
        print("You have signed in " + AnotherAccountName +"\n")

    loop = input("Want to make another account? : ")
    if loop == 'yes':
        UsersMulti()
    else:
        done()
    



    Usernames = [Username]
    Passwords = [Password]
    

    
#user and pass and ask to sign in
def SignUp():
    global AccountName
    AccountName = input("Real Name : ")
    User = input("Username : ")
    Pass = input("Password : ")

    print("\nNow you're going to sign in ⬇️\n")

    UserType = input("User : ")
    UserPass = input("Pass : ")

    if UserType == User and UserPass == Pass:
        print("\nYou have signed in ✅\n")
    else:
        print("\n Incorrect password or username ❌\n") 
    
    Trans = input("Want to create another account? : ")
    
    if Trans == "yes":
        UsersMulti()
    elif Trans == "no":
        done()

def SignIn():
    pass
def StartUp():
    InUp = input("Do you want to sign in or sign up for a account? : ")
    if InUp == "sign up":
        SignUp()
    if InUp == "sign in":
        pass

StartUp()




    

