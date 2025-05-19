import numpy as np


def random_predict(number:int=1) -> int:
    """Сначала устанавливаем любое random число, а потом находим новое
    random число, но с измененным диапазоном (где на границе уже проверенное random число)
    в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    random_array_min = [1]
    random_array_max = [101]
    
    while number != predict:
        count += 1
        if number > predict:
            random_array_min.append(predict)
            predict = np.random.randint(max(random_array_min)+1, min(random_array_max))               
        elif number < predict:
            random_array_max.append(predict)
            predict = np.random.randint(max(random_array_min), min(random_array_max))

    return count


print(f'Количество попыток: {random_predict()}')


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток

    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


# RUN
score_game(random_predict)


if __name__ == '__main__':
    score_game(random_predict)