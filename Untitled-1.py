# *************************************
# РАЗДЕЛ ИМПУРТА МОДУЛЕЙ
# *************************************
import random
# *************************************
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
# *************************************
# функция настроек
def nastroyki():
    print("ПРЕДСТАВЛЯЕМ ИГРУ 'НАПЁРСТКИ'")
    print()
    print("Автор:Nastik_Vu")
    print()             
    print("Версия 1.0")
    print()
    
    print("Введите сколько у вас деньжат")
    dengi = input()
    while True:
        if dengi.isdigit():
            dengi = int(dengi)
            break
        else:
            print("НАПИШИТЕ ТОЛЬКО ЦИФРЫ!")
            dengi = input()
            
    print("Теперь хм....,ладно,размер твоей ставки?")
    miniStavka = input()
    while True:
        if miniStavka.isdigit():
           miniStavka = int(miniStavka)
           break
        else:
            print("Ну что же такое!Цифры!Цифры!!")
            miniStavka = input()

    return [dengi,miniStavka]
def intro():
    print('''Расхаживаете вы по рынку.
    На рынке вы осматриваете ларьки,ваш взгляд попал на ларёк с мужчиной.
    Он крепко спал,вы его разбудили и спросили что тут продаётся.
    мужчина засмеялся <Ха Ха Ха! Расмешил!> и вы спросили <А что не так?>-возразили вы
    мужчина с усмешкой спросил-<Видишь напёрстки?> вы ответили тогда мужчина положил деньги на стол
    вы спросили-<Что это значит?!> к вам подошли много людей и один мужчина
    обьяснил-<Вы молодой человек идёте на риск,риск потерять денги!Это игра
    очень запутанна,игра называется Напёрстки,есть шарик и три стаканчика из бумаги>
    <И что!>-перебили его вы-<Я вспомнил что за игра...>''')

def proverka(dengi,miniStavka):
    print("Ну гражданин,сделай свою ставку.")
    stavka = input()
    while True:
        if stavka.isdigit():
            # переводи чесло в строку
            stavka = int(stavka)
            # проверяем что ставка больше минимальной
            if stavka > miniStavka:
                # проверяем что ставка меньше минимальной
                stavka = input()
                    # проверяем что ставка больше количества денег
                if stavka > dengi: 
                    print("Гражданин,у вас денег мало,мол сделай ставку поменьше")
                    stavka = input()
                else:
                    break
        return stavka

def sravnenie(naperstok,naperstokigroka):
    if naperstok == naperstokigroka:
        sovpadenie = True
    else:
        sovpadenie = False
    return sovpadenie
def intro2():
    print(''' После того мужчина вам говорит <Ну мол давай ставку>
    Вы дали свои последние деньги и сказали:
    <Эх, ладно вот> мужчина начал быстро быстро вертеть напёрстки по столу.Он резко остановил
    напёрстки и с ухмылкой сказал <Ну мол выберай> вы думали где шарик....''')

def otvet():
    while True:
        if nap.isdigit():
            if (nap in '123') and (len(nap)==1):
                nap = int(nap)
                break
        else:
            print("Надо ввести только числа 1,2,3")
            nap = int(nap)
    else:
        print("Надо вводить цифры мол а не буквы")
        nap = input
    return nap

def playAgain():
# создаём бесконечный цикл
    while True:
        print("Мол сыграть еще не хочешь?")
        otvet = input()
        otvet = otvet.lower
        # задаем вопрос и получаем ответ
        if (otvet == "да") or (otvet == "д") or (otvet == "yes") or (otvet == "Yes") or (otvet == "YES"):
            return True
        #проверяем ответ на совпадение со следущими фразами
        #"да","Да","ДА","д","y","yes","Yes","YES"
        # если есть совпадение то переменной присваеваем значение True
        # и пререваем цикл  камандой retur
        elif (otvet == "Нет") or (otvet == "НЕТ") or (otvet == "нет") or (otvet == "n") or (otvet == "No") or (otvet == "NO"):
            return False
        print("Игра закончина")
        break
        # проверяем ответ на совпадение со следущими фразами
        # "Нет","нет","НЕТ","No","n","NO"
        # если есть совпадение то переменной присваеваем значение  False

        # если совпадений с первыми двумя случаеми нет
        # гововорим ползавателю что не понили его ответа
    else:
        print("Я не понимаю тебя,мол скажи понятно")

# *************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# *************************************
many,minBig = nastroyki()
intro()

while True:
    stavkaIgroka = proverka (many,minBig)
    intro2() 
    napG = random.randint(1,3)
    napI = otvet()
    if sravnenie(napG,napI):
        print("Мол Бог выбрал что ты выйграл!")
        many = many + stavkaIgroka
    else:
        print("Мол проиграл!")
        many = many - stavkaIgroka

    if many > minBig:
        # зададим вопрос хочет ли пользователь сыграть ещё
        if playAgain():
            print('Продолжаем играть.В наличии'+str(many))
        else:
            print('Ну мол ладненько.В ниличии'+str(many))
            break
    else:
            print("У вас мол мало денег")
            print("У вас в наличии"+str(many)+".Игра будет закончена.")
            break

