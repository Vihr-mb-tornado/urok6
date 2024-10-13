import person

human = Person(name='Вася', money=10.0, mood=50, health=100)

print(human)

'''
human = Person(name='Тарас', money=0, mood=100, health=100)

print(human)
# === Тарас ===
# Здоров'я: 100
# Настрій: 100
# Капітал: 0

human.change_state(
         money = 100,
         mood = -20,
         health = -5
     )

print(human)
# === Тарас ===
# Здоров'я: 95
# Настрій: 80
# Капітал: 100
'''
