import time,sys,random

def incorrect():
    print("!Missing or Incorrect Keying! ")

def add_dot():
    print(".")
    time.sleep(.3)
    print("..")
    time.sleep(.3)
    print("...")
    time.sleep(.3)

class player():
    def __init__(self,name,health=10,power=100,puan=0):
        self.name = name
        self.health = health
        self.power = power
        self.puan = puan
    def show_information(self):
        print("""
        Name = {}
        Health = {}
        Power = {}
        Puan = {}
        """.format(self.name,self.health,self.power,self.puan))
    def attack(self,enemy):
        result = self.attack_defence()
        if (result == 1):
            print("Attack Successful")
            self.power -= 8
            self.puan += 10
            enemy.health -= 1
            self.show_information()
            enemy.show_information()
        else:
            print("Attack Failed")
            self.power -= 8
            self.health -= 1
            enemy.puan += 10
            self.show_information()
            enemy.show_information()
    def defence(self,enemy):
        result = self.attack_defence()
        if (result == 1):
            print("Defense Successful!")
            enemy.power -= 8
            self.puan += 10
            enemy.health -= 1
            self.show_information()
            enemy.show_information()
        else:
            print("Defense Failed!")
            enemy.power -= 8
            enemy.puan += 10
            self.health -= 1
            self.show_information()
            enemy.show_information()
    def attack_defence(self):
        return random.randint(1,2)
    def exit(self):
        print("Game Shutting Down...")
        add_dot()
        sys.exit()

player1 = player("Ahmet")
player2 = player("Mehmet")

print("Game Launching...")
add_dot()

while True:
    movement = input("""
    1-Attack
    2-Defence
    3-Exit
    Choice of Move:""")
    if(movement == "1"):
        player1.attack(player2)
    elif(movement == "2"):
        player1.defence(player2)
    elif(movement == "3"):
        player1.exit()
    else:
        incorrect()
    if(player1.puan == 100 or player2.health == 0 or player2.power<=0):
        print("The winner of the game:",player1.name)
        break
    if(player2.puan ==100 or player1.health == 0 or player1.power<=0):
        print("The winner of the game:", player2.name)
        break
