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

def proverka()
    print("Ну гражданин,сделай свою ставку.")
    stavka = input()
    while True:
        if stavka.isdigit():
            # переводи чесло в строку
            stavka = int(stavka)
                # проверяем что ставка больше минимальной
            if stavka > miniStavka
                # проверяем что ставка меньше минимальной
            else:
                print("Мол ставка меньше не может!")
                stavka = input()
                # проверяем что ставка больше количества денег
                if stavka > dengi
            else:
                print("Гражданин,у вас денег мало,мол сделай ставку поменьше")
                stavka = input()
                return stavka

# *************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# *************************************
many,minBig = nastroyki()
intro()
stavkaIgroka = proverka(many,minBig)