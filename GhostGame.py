#Ghost Game
import random
from random import randint
feel = True
score = 0
while feel == True:
    print("Привет, дружочек! Этот дом полон различных дверей...")
    print("За одной из них призрак... Попробуй на него не нарваться!")
    print("Перед тобой 3 двери, какую выберешь? :)")
    door = randint(1, 3)
    a = int(input("1, 2, или 3?"))
    if a == door:
        print("О нет, тут призрак! Бежим!")
        feel = False
    elif a != door:
        print("Ну что, а ты хорош! Идем дальше!")
        score = score + 1
    else:
        print("Error!")
        feel = False
print("Ты набрал: ", score, " очков")