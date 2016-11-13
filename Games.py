import random
import turtle
import sys

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_line(from_x, from_y, to_x, to_y):
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)

def draw_gibbet(step):
    if step == 1:
        # столб
        draw_line(-160, -100, -160, 80)
    elif step == 2:
        # горизонтальная балка
        draw_line(-160, 80, -80, 80)
    elif step == 3:
        # косая черта - ребро жесткости
        draw_line(-160, 40, -120, 80)
    elif step == 4:
        # веревка
        draw_line(-100, 80, -100, 40)
    elif step == 5:
        gotoxy(-100,0)
        turtle.circle(20)
    elif step == 6:
        # туловище
        draw_line(-100, 0, -100, -50)
    elif step == 7:
        # левая рука
        draw_line(-100, -10, -120, -20)
    elif step == 8:
        # правая рука
        draw_line(-100, -10, -80, -20)
    elif step == 9:
        # левая нога
        draw_line(-100, -50, -120, -60)
    elif step == 10:
        # правая нога
        draw_line(-100, -50, -80, -60)

x = random.randint(1, 100)

print('Случайное число: ', x)

turtle.speed(0)
turtle.color('blue')


gotoxy(-200, 250)
turtle.write('Я загадал число \n Попробуй угадать',
             font = ('Arial', 18, 'normal'))

answer = turtle.textinput('Хотите поиграть?' , 'y/n')
if answer == 'n':
    sys.exit(9)

hints = False
answer = turtle.textinput('Давать подсказки?' , 'y/n')
if answer == 'y':
    hints = True

try_count = 0

while True:
    number = turtle.numinput('Попробуй угадать', 'Число', 0, -10, 100)

    if hints:
        gotoxy(100, 200 - try_count * 12)
        if number < x:
            turtle.write(str(number) + ' Загаданное число больше')
        else:
            turtle.write(str(number) + ' Загаданное число меньше')


    if number == x:
        gotoxy(-150, -200)
        turtle.color('green')
        turtle.write('Ура! Ты победил!', font=('Arial', 20, 'normal'))
        break
    elif number == -5:
        sys.exit(5)
    else:
        gotoxy(-150, 100)
        turtle.color('red')
        turtle.write('Неверно!', font=('Arial', 20, 'normal'))
        try_count += 1
        draw_gibbet(try_count)

        if try_count == 10:
            gotoxy(-150, 150)
            turtle.color('red')
            turtle.write('Ты проиграл, дружок... ха-ха-ха!',
                         font=('Arial', 20, 'normal'))
            break


#input()