import random
# подключили модуль random
print("Преветствую вас в игре Угодайка число,выбери имя твоего игрока")
myName = input()
# Поздоровались, спросили имя, ответ записали в переменную myName
s = random.randint (1,100)
print("Я загадал число от 1 до 100")
# программа загадал (сгенерировал) число от 1 до 17 и рассказал об этом игроку
for i in range(10):
    # даём игроку 10 попытки отгодать число от 1 до 100")
    y = input()
    # программа просит ввести число и записывает введённое в переменну y
    while True:
        if y.isdigit():
            break
        else:
            print("Забыл?Введи число!!")
            y = int(y)
    # переводи число в строку
    if s > y:
    print("Ваше чесло меньше загадонного")
    if s < y:
    print("Ваше число больше загадонного")
    if s == y:
        break
if s == y:
 print("Ты выйграл молодец!")
if s != y:
    print("Ты проиграл!Не печалься!Я скажу число которое загадал,это"+str(s))