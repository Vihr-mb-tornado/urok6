import random
class Action:
    name = ''
    health = 0
    mood = 0
    money = 0

    def __init__(self, name, health, mood, money ):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

class Work (Action):
    def __init__(self, name, health, mood, money):
        Action.__init__(self, name, health, mood, money)

class Rest (Action):
    def __init__(self, name, health, mood, money):
        Action.__init__(self, name, health, mood, money)

class Person:
    name = ''
    health = 100
    mood = 50
    money = 10.50

    def __init__(self, name, health, mood, money ):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return f' -< {self.name} >- ' \
            f' Здоров`я: {self.health}'\
            f' Настрій: {self.mood}'\
            f' Гроші: {self.money}'

    def is_alive(self):
        if (self.health<=0) or (self.mood<=0) or (self.money<=0):
            return False
        else:
            return True

    def change_state(self, health, mood, money):
        self.health = self.health + health
        if self.health<=0:
            self.health=0
            print(f'{self.name}: помер')

        self.mood = self.mood + mood
        if self.mood<=0:
            print(f'{self.name}: нема настрою')

        self.money = self.money + money
        if self.money<=0:
            print(f'{self.name}: нема грошей')

    def do(self, act: Action):

        #Якщо переданий об'єкт класу Work - те саме, що і з Action,
        #тільки якщо значення настрою більше 90, то грошей має додатись на 10% більше;
        if type(act) == Work:
            if act.mood>90:
                act.money=act.money+act.money*0.1

        #Якщо переданий об'єкт класу Rest - те саме, що і з Action,
        #тільки якщо значення здоров'я менше 40, то настрої має додатись на 20% менше;
        if type(act) == Rest:
            if act.health<40:
                act.mood=act.mood-act.mood*0.2

        self.change_state(act.health, act.mood, act.money)