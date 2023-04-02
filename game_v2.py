'''Игра угадай число
Компьютер сам загадывает и угадывает число
'''

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,101) #предополагаемое число
        if number == predict_number:
            break
        
    return(count)

def score_game(random_predict) -> int:
    """За какое кол-во попыток в среднем угадывает наш подход

    Args:
        random_predict (_type_): вункция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) #фиксируем сид для производимости
    random_array = np.random.randint(1, 101, size=1000) #загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш адгоритм угадывает число в среднем за: {score} попыток')
    return score

score_game(random_predict) #RUN
