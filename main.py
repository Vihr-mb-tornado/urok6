import random
from person import Person
from person import Action

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
            a = Action('відпочинок', random.randint(0, 50), random.randint(0, 50), float(random.randint(-50, 0)))
        else:
            a = Action('праця', random.randint(-20, 20), random.randint(-20, 20), float(random.randint(0, 50)))
        human.do(a)
        print(human)
    if not l[0].is_alive() and not l[1].is_alive() and not l[2].is_alive():
        print('To be Continued')
        break

#h = Person('Кхы', 50, 50, 10.00)
#a = Action('пішов працювати', -1,-1, 10.0)
#print(h)
#h.do(a)
#print(h)
'''

'''

