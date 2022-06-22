# 2) Добавить в функцию числовой лимит
# 3) Добавить в функцию вариант замены элементов
# 4) Отрефакторить

def run_fizz_buzz() -> None:
    """Run FizzBuzz game"""

    for number in range(1, 20):
        fizz_buzz = ''

        if number % 3 == 0:
            fizz_buzz += 'Fizz'

        if number % 5 == 0:
            fizz_buzz += 'Buzz'

        print(fizz_buzz or number)


if __name__ == '__main__':
    run_fizz_buzz()
