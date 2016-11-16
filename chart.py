from tkinter import *
import math

root = Tk()
root.title('Построение графика функции y = sin(x)')
root.geometry('1320x640') # размер окна

canvas = Canvas(root, width = 1040, height = 640, bg = '#002')
canvas.pack(side = 'right') # отображение

#линии сетки по вертикали
for y in range(21):
    k = 50 * y
    canvas.create_line(20 + k, 620, 20 + k, 20, width = 1, fill = '#191938')

#линии сетки по горизонтали
for x in range(13):
    k = 50 * x
    canvas.create_line(20, 20 + k, 1020, 20 + k, width = 1, fill = '#191938')

#линии координат
canvas.create_line(20, 20, 20, 620, width = 1, arrow = FIRST, fill = 'white')
canvas.create_line(10, 320, 1020, 320, width = 1, arrow = LAST, fill = '#ffffff')

canvas.create_text(20, 10, text = '300', fill = 'white')
canvas.create_text(20, 630, text = '-300', fill = 'white')
canvas.create_text(10, 310, text = '0', fill = 'white')
canvas.create_text(1020, 310, text = '1000', fill = 'white')

lable_w = Label(root, text = 'Циклическая частота:')
lable_w.place(x = 0, y = 10)
lable_phi = Label(root, text = 'Смещение графика по Х:')
lable_phi.place(x = 0, y = 30)
lable_A = Label(root, text = 'Амплитуда:')
lable_A.place(x = 0, y = 50)
lable_dy = Label(root, text = 'Смещение графика по Y:')
lable_dy.place(x = 0, y = 70)

entry_w = Entry(root)
entry_w.place(x = 150, y = 10)
entry_phi = Entry(root)
entry_phi.place(x = 150, y = 30)
entry_A = Entry(root)
entry_A.place(x = 150, y = 50)
entry_dy = Entry(root)
entry_dy.place(x = 150, y = 70)

# x(t) = A * sin(w * t + phi)

def sinus(w, phi, A, dy):
    global sin
    sin = 0
    xy = []
    for x in range(1000):
        y = math.sin(x * w)
        xy.append(x + phi)
        xy.append(y * A + dy)
    sin = canvas.create_line(xy, fill = 'blue')

def clean():
    canvas.delete(sin)

btn_calc =  Button(root, text = 'Расчитать')
btn_calc.bind('<Button-1>', lambda event: sinus(float(entry_w.get()),
                                                float(entry_phi.get()),
                                                float(entry_A.get()),
                                                float(entry_dy.get())))
btn_calc.place(x = 10, y = 100)
btn_clean =  Button(root, text = 'Очистить')
btn_clean.bind('<Button-1>', lambda event: clean())
btn_clean.place(x = 100, y = 100)

root.mainloop()
