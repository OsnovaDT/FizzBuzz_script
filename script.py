# 3) Добавить в функцию вариант замены элементов
# 4) Отрефакторить

def run_fizz_buzz(max_number: int) -> None:
    """Run FizzBuzz game"""

    for number in range(1, max_number + 1):
        fizz_buzz = ''

        if number % 3 == 0:
            fizz_buzz += 'Fizz'

        if number % 5 == 0:
            fizz_buzz += 'Buzz'

        print(fizz_buzz or number)


if __name__ == '__main__':
    run_fizz_buzz(16)
