#Напишите программу, которая по заданному номеру четверти,
#показывает диапазон возможных координат точек в этой четверти (x и y).

X = int(input('Введи номер четверти:  '))
if X==1:
    print('Координата Х лежит в диапазоне от 0 до +∞,Координата Y лежит в диапазоне от 0 до +∞')
elif X==2:
    print('Координата Х лежит в диапазоне от -∞ до 0,Координата Y лежит в диапазоне от 0 до +∞')
elif X==3:
    print('Координата Х лежит в диапазоне от -∞ до 0,Координата Y лежит в диапазоне от -∞ до 0')
elif X==4:
    print('Координата Х лежит в диапазоне от 0 до +∞,Координата Y лежит в диапазоне от -∞ до 0')
else:
    print('В декартовой системе координат всего 4 четверти, учи алгебру')