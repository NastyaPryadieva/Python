# *******************************
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# *******************************
import random

# *******************************
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
# *******************************
def genVis():
    HANGMAN_PICT = ['''
    +---+
        |
        |
        |
       ===''','''
    +---+
    O   |
        |
        |
       ===''',''' 
    +---+
    O   |
    |   |
        |
       ===''','''
    +---+
    O   |
    |   |
   ( )  |
       ===''','''
     +---+
     O   |
    /|\  |
    ( )  |
        ===''']

    return HANGMAN_PICT

def genSlov():
    words = 'аист акула баран бубуин барсук бобр верблюд голубь гусь'.split()
    return words

def vyborSlova(spis):
    indSl = random.randint(0,len(spis)-1)
    slovo = spis[indSl]
    return slovo

def proverka(strbukv):
    while True:
        print('Введите букву')
        buk = input()
        buk = buk.lower()
        if len(buk) != 1:
            print('Надо ввести толькоодну букву')
        elif buk not in 'йцукенгшщзхъфывапролджэячсмитьбю':
            print('Надо ввести только рускую букву')
        elif buk in strbukv:
            print('Вы уже называли эту букву')
        else:
            return buk


def displayBoard(nasyVis,errorBuk,yesByk,sicretSl):
    print(nasyVis[len(errorBuk)])
    print()
    print('Ошибочные буквы'+errorBuk)
    print()

    shablon = '_'*len(sicretSl)

    for i in range(len(sicretSl)):
        if sicretSl[i] in yesByk:
            shablon = shablon[:i]+sicretSl[i]+shablon[i+1:]

    for s in shablon:
        print(s,end=' ')
    print()

def playAgain():
# создаём бесконечный цикл
    while True:
        print("Ты не хочешь сыграть ещё?")
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
        print("Я не понимаю тебя")


# *******************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# *******************************

vis = genVis()
wordsS = genSlov()
sicretSlovo = vyborSlova(wordsS)
print(sicretSlovo)
strokaErrorB = ''
strokaYesB = ''

while True:
    displayBoard(vis,strokaErrorB,strokaYesB,sicretSlovo)
    vvedenayaB = proverka(strokaErrorB+strokaYesB)