"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def guess_number(random_predict) -> int:
    """В этой функции мы используем бинарный поиск для угадывания числа.
    Начальный диапазон поиска задается значениями 1 и 100
    (т.к. число находится в диапазоне от 1 до 100).
    Затем мы сравниваем загаданное число с предполагаемым числом
    и сужаем диапазон поиска в соответствии с результатом сравнения."""
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count = 0
        low = 1
        high = 100
        guess = (low + high) // 2

        while guess != number:
            count += 1
            if guess > number:
                high = guess - 1
            else:
                low = guess + 1
            guess = (low + high) // 2

        count_ls.append(count)

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    guess_number(random_predict)
    #score_game(random_predict)
