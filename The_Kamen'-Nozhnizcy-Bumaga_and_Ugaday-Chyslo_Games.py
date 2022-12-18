import easygui
import random


def rock_paper_scissors():
    title = '"Камень, ножницы, бумага"'
    choices = ['Камень', 'Ножницы', 'Бумага']
    scripts = {'Камень':'Камень.png', 'Ножницы':'Ножницы.png', 'Бумага':'Бумага.png'}
    easygui.msgbox('Добро пожаловать в игру "Камень, ножницы, бумага"!!!', title, "Ок")
    easygui.msgbox('Правила игры просты: камень бъёт ножницы, ножницы --- бумагу, а бумага --- камень.' + '\nПобедитель получает целый мешок ничего!' + '\nГотовы?' + '\nНа старт!' + '\nВнимание!', title, 'Поехали!')
    while True:
        play = easygui.buttonbox('Выбери камень, ножницы, или бумагу: ', title, choices=choices)
        comp = random.choice(choices)
        if (play == 'Камень' and comp == 'Ножницы') or (play == 'Ножницы' and comp == 'Бумага') or (play == 'Бумага' and comp == 'Камень'):
            message = 'Вы обыграли компьютер!!! Вот Ваш мешок ничего!'
            button = 'Ура, победа!'
        elif (play == 'Ножницы' and comp == 'Камень') or (play == 'Бумага' and comp == 'Ножницы') or (play == 'Камень' and comp == 'Бумага'):
            message = 'Лузер!!! Тебя обыграл компьютер, ничтожество!!! Вот Ваш мешок ничего, господин компьютер!'
            button = 'Пацан к успеху шёл...'
        elif (play == 'Камень' and comp == 'Камень') or (play == 'Ножницы' and comp == 'Ножницы') or (play == 'Бумага' and comp == 'Бумага'):
            message = 'Ха, Вы с компьютером сыграли вничью!!! Бывает, же... Ну и хорошо, я тогда мешок ничего у себя оставлю.'
            button = 'Очередная победа дружбы'
        easygui.msgbox(message, title, button, image = (scripts[play], scripts[comp]))
        out = easygui.buttonbox('Хотите сыграть ещё?', title, choices=("Да", "Нет", "Выход"))
        if out == "Нет":
            break
        elif out == "Выход":
            global RES
            RES = None
            break

def guess_the_number():
    title = '"Угадай число"'
    easygui.msgbox('Добро пожаловать в игру "Угадай число"!!!', title, "Ок")
    easygui.msgbox('Правила игры просты: компьютер загадывает некое целое число от 0 до 1000, а Вы должны его угадать, и как можно быстрее.' + '\nВедь от количества попыток зависит размер Вашей награды --- целого (или не очень) мешка ничего!' + '\nГотовы?' + '\nНа старт!' + '\nВнимание!', title, 'Поехали!')
    while True:
        comp = random.randint(0, 1000)
        answ = None
        shch = 0
        while answ != comp:
            shch += 1
            answ = easygui.integerbox("Какое число загадал компьютер?", title, default=0, lowerbound=0, upperbound=1000)
            if answ == None:
                answ = 0
            if answ < comp:
                easygui.msgbox('Ваше число меньше загаданного.', title, ":(")
            elif answ > comp:
                easygui.msgbox('Ваше число больше загаданного.', title, ":(")
        else:
            easygui.msgbox('Поздравляем, вы угадали число, задуманное компьютером!!! Это было число ' + str(comp) + "!", title, "Ура, победа!!!")
            if shch <= 1:
                prize = "супер-пупер-мега-экстра-гига-киломешок ничего"
                button = "Боги удачи любят Вас"
            elif 2 <= shch <= 5:
                prize = "супер-пупер мешок ничего"
                button = "Лайф кулд би дрим"
            elif 6 <= shch <= 8:
                prize = "большой мешок ничего"
                button = "Стонкс"
            elif 9 <= shch <= 12:
                prize = "обычный мешок ничего"
                button = "Ура, победа!"
            elif 13 <= shch <= 15:
                prize = "небольшой мешок ничего"
                button = "Чел харош"
            elif 16 <= shch <= 20:
                prize = "маленький мешок ничего"
                button = "Поясни за свою маленькость"
            elif 21 <= shch <= 25:
                prize = "микромешок ничего"
                button = "Не, ну тут нужен мискроскоп"
            elif 25 <= shch:
                prize = "наномешок ничего"
                button = "Говорят, он меньше планковской длины"
            easygui.msgbox('На это у Вас ушло ' + str(shch) + ' попыток. Ваша награда --- ' + prize + '!!!', title, button)
        out = easygui.buttonbox('Хотите сыграть ещё?', title, choices=("Да", "Нет", "Выход"))
        if out == "Нет":
            break
        elif out == "Выход":
            global RES
            RES = None
            break
        



games = [
    'Камень, ножницы, бумага',
    'Угадай число',
    'Выход'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

RES = True

while RES:
    res = easygui.buttonbox('Выбери игру!', "Меню", choices=games)
    if res is None or res == 'Выход':
        break
    games_entry_points[games.index(res)]()