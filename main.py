import random
from person import Person
#l = []
human0 = Person('Вася', 50, 50, 10.00)
human1 = Person('Петя', 50, 50, 10.00)
human2 = Person('Александр', 50, 50, 10.00)
l = [human0, human1, human2]

while True:
    for human in l:
        # праця (додає гроші, забирає здоров'я та настрій)
        # відпочинок (додає настрій та здоров'я, але може відібрати гроші).
        if random.randint(0, 1):
            h=random.randint(0, 50)
            md=random.randint(0, 50)
            mn=float(random.randint(-50, 0))
        else:
            h=random.randint(-20, 20)
            md=random.randint(-20, 20)
            mn=float(random.randint(0, 50))
        human.change_state(h, md, mn)
        print(human)
    if not l[0].is_alive() and not l[1].is_alive() and not l[2].is_alive():
        print('To be Continued')
        break
'''

'''
