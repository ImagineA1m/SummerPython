    #example
'''
x = 1
if x == 1:
    print("hey it works!")

else:
    print("too bad")
'''
    #chatbot

def output():
    print("Hi you are " + age + " years old and your name is " + name + " !" )  
def goals():#1
        print("Nice having goals or plans is helpful to get better or do something")
def ageres():#2
     print("Why should i tell you my age if you didn't tell yours?")
def botage():#3
    print("I'm 39 years old")
def botname():#4
    print("My name is Jason")
def hobbies():#5
     print("I can't do any hobbies since im a bot but you can")
def fears():#6
     print("i have Acrophobia: Fear of heights.")





def main():
    global age 
    global name

    age = input("Hi, how old are you?  :")
    if age.__contains__("no"):
        print("Ok no age why not tell me your name  :")
    name = input("Whats your name  : ")
    ask = input("do you want me to tell you your name and age?    : ")
    if ask == "yes":
        output()
    topic = input("ok " + name + " what do you want to talk about. We can talk about \n Goals \n age \n hobbies \n fears \n What do you want :  ")
    if topic.__contains__("Goals") or topic.__contains__("Plans"):
         goals()
    if topic.__contains__("age") and age == ("no"):
         ageres()
    else:    
        botage()
    if topic.__contains__("hobbies"):
         hobbies()
    if topic.__contains__("fears"):
         fears()


main()


'''

global var 

or

function(var)

'''








    







    


