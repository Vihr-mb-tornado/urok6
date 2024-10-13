﻿import random
from operator import length_hint

from person import Person
from person import Action
from person import Rest
from person import Work

human0 = Person('Вася', 50, 50, 10.00)
human1 = Person('Петя', 50, 50, 10.00)
human2 = Person('Александр', 50, 50, 10.00)
l = [human0, human1, human2]

while True:
    for human in l:
        # праця (додає гроші, забирає здоров'я та настрій)
        # відпочинок (додає настрій та здоров'я, але може відібрати гроші).
        if random.randint(0, 1):
            a = Rest('відпочинок', random.randint(0, 50), random.randint(0, 20), float(random.randint(-50, 0)))
        else:
            a = Work('праця', random.randint(-20, 20), random.randint(-20, 0), float(random.randint(0, 50)))
        human.do(a)
        print(human)
        # Видаляемо вибувших
        if not human.is_alive():
            print(human.name + " вибув")
            l.remove(human)

    if len(l)==0:
        print('To be Continued')
        break

#h = Person('Кхы', 50, 50, 10.00)
#a = Action('пішов працювати', -1,-1, 10.0)
#print(h)
#h.do(a)
#print(h)
'''

'''

