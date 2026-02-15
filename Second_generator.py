import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генератор, який ітерує по всіх дійсних числах у тексті.
    Дійсні числа знаходяться за допомогою регулярних виразів.
    """
    # Регулярний вираз шукає числа (цілі або з плаваючою крапкою), 
    # які обрамлені межами слів (\b). Це відповідає умові "чітко відокремлені".
    pattern = r'\b\d+(?:\.\d+)?\b'
    
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    """
    Обчислює загальну суму чисел у вхідному рядку, використовуючи переданий генератор.
    """
    # func(text) повертає генератор, sum() підсумовує всі значення, які він видає
    return sum(func(text))

# Приклад використання:
if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
