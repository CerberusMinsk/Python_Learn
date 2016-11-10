from tkinter import *
import math

root = Tk()
root.title('Построение графика функции y = sin(x)')
root.geometry('1020x620') # размер окна

canvas = Canvas(root, width = 1020, height = 620, bg = '#002')

#линии сетки по вертикали
for y in range(21):
    k = 50 * y
    canvas.create_line(10 + k, 610, 10 + k, 10, width = 1, fill = '#191938')

#линии сетки по горизонтали
for x in range(13):
    k = 50 * x
    canvas.create_line(10, 10 + k, 1010, 10 + k, width = 1, fill = '#191938')

#линии координат
canvas.create_line(10, 10, 10, 610, width = 1, arrow = FIRST, fill = 'white')
canvas.create_line(0, 310, 1010, 310, width = 1, arrow = LAST, fill = '#ffffff')

# x(t) = A * sin(w * t + phi)
w = 0.0209 # циклическая частота
phi = 10   # смещение графика по Х
A = 200    # амплитуда
dy = 310   # смещение графика по Y

xy = []
for x in range(1000):
    y = math.sin(x * w)
    xy.append(x + phi)
    xy.append(y * A + dy)

sin_line = canvas.create_line(xy, fill = 'blue')

canvas.pack() # отображение
root.mainloop()
