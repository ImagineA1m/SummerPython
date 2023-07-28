def main():
    pass
def start():
    pass
def Whowins():
    pass
def rounds():
    pass
def humanChoice():
    choices=["rock","paper","scissors"]
    human = input("choose rps : ")
    if (human in choices):  
        compChoice()
    else:
        humanChoice()
humanChoice()

def compChoice():
    print("123")
    








# def rps():
#     x, y = input("1 player then next player: example[p1,p2] : ").split()  
#     if x == y:
#         print("Both players selected {x}. It's a tie!")
#     elif x == "rock":
#         if y == "scissors":
#             print("p1 You win!")
#         else:
#             print("p1 You lose.")
#     elif x == "paper":
#         if y == "rock":
#             print("p1 You win!")
#         else:
#             print("p1 You lose.")
#     elif x == "scissors":
#         if y == "paper":
#             print("p1 You win!")
#         else:
#             print("p1 You lose.")
# rps()