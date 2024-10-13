# import random
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
        return f' -< {self.name} >- \n' \
            f' Здоров`я: {self.health}\n'\
            f' Настрій: {self.mood}\n'\
            f' Грощі: {self.money}\n'

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



