'''Игра: Угадай число
Компьютер сам загадывает и отгадывает число
Необходимо чтобы программа находила число меньше чем за 20 попыток
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
    
    # Именуем аргуметы предполагаемого числа для дальнейшего изменения
    a = 1
    b = 101
    predict_number = np.random.randint(a,b) #Предополагаемое число
    
    while True:
        count += 1
        if number == predict_number:
            break
        elif number < predict_number:
            b = predict_number
            predict_number = np.random.randint(a, b)
        elif number > predict_number:
            a = predict_number
            predict_number = np.random.randint(a,b)
            
        
    return(count)

def score_game(random_predict) -> int:
    """За какое кол-во попыток в среднем угадывает наш подход

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) #фиксируем сид для производимости
    random_array = np.random.randint(1, 101, size=1000) #загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

score_game(random_predict) #RUN
