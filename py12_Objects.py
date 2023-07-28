import random
import time

class Giant:
    def __init__(self, name, health,strength):
        self.name = name
        self.health = health
        self.strength = strength
    def attack(self,opponent):
        damage = random.randint(0,self.strength)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} and deals {damage} damage.")
    def is_alive(self):
        return self.health > 0
        
    
#
class Robot(Giant):
    def __init__(self, name, health, strength, laser_eye):
        super().__init__(name, health, strength)
        self.laser_eye = laser_eye

    def attack(self, opponent):
        damage = random.randint(self.laser_eye, self.strength)
        opponent.health -= damage
        print(f"{self.name} slashes with his sword, dealing {damage} damage to {opponent.name}.")
    

class Brawler:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, opponent):
        damage = random.randint(1, self.strength)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} and deals {damage} damage.")

    def is_alive(self):
        return self.health > 0

class Swordsman(Brawler):
    def __init__(self, name, health, strength, sword_skill):
        super().__init__(name, health, strength)
        self.sword_skill = sword_skill

    def attack(self, opponent):
        damage = random.randint(self.sword_skill, self.strength)
        opponent.health -= damage
        print(f"{self.name} slashes with his sword, dealing {damage} damage to {opponent.name}.")



def main():
    # Create brawlers
    giant1 = Giant("Jojo", health=180 , strength=50)
    robot1 = Robot("Mech", health=80,strength=100, laser_eye=90)
    brawler1 = Brawler("Joe", health=100, strength=20)
    swordsman1 = Swordsman("Arthur", health=100, strength=18, sword_skill=10)

    # Battle loop
    while brawler1.is_alive() and swordsman1.is_alive() and giant1.is_alive and robot1.is_alive:
        brawler1.attack(swordsman1)
        if not swordsman1.is_alive():
            break
        swordsman1.attack(brawler1) 
        
        
        
        
        if not brawler1.is_alive():
            break
        time.sleep(1)

    # Determine the winner
    if brawler1.is_alive():
        print(f"{brawler1.name} wins the battle!")
    elif swordsman1.is_alive():
        print(f"{swordsman1.name} wins the battle!")
    elif giant1.is_alive():
        print(f"{giant1.name} wins the battle!")
    elif robot1.is_alive():
        print(f"{robot1.name} wins the battle!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()