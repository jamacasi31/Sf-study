'''Игра угадай число'''

import numpy as np

number = np.random.randint(1,101) #загадываем число

count = 0 #кол-во попыток

while True:
    count += 1
    predict_number = int(input('Угадай число от 1 до 101 '))
    
    if predict_number > number:
        print('Загаданное число меньше')
    elif predict_number < number:
        print('Загаданное число больше')
    else:
        print(f"Вы угадали! Загаданное число{number}, за {count} попыток")
        break #выход из цикла