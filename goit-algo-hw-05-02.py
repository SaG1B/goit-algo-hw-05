import re
from typing import Callable


def generator_numbers(text: str):
    """
    Генератор, який знаходить всі дійсні числа в тексті
    """
    # шукаємо числа з плаваючою точкою
    pattern = r"\b\d+\.\d+\b"

    for match in re.findall(pattern, text):
        yield float(match)


def sum_profit(text: str, func: Callable):
    """
    Обчислює суму всіх чисел через генератор
    """
    return sum(func(text))


# ===== ПРИКЛАД ВИКОРИСТАННЯ =====

if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими "
        "надходженнями 27.45 і 324.00 доларів."
    )

    total_income = sum_profit(text, generator_numbers)

    print(f"Загальний дохід: {total_income}")