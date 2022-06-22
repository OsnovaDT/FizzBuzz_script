# 4) Отрефакторить

def run_fizz_buzz(
        max_number: int, replacement_options={3: 'Fizz', 5: 'Buzz'}) -> None:
    """Run FizzBuzz game"""

    for number in range(1, max_number + 1):
        fizz_buzz = ''

        for key, value in replacement_options.items():
            if number % key == 0:
                fizz_buzz += value

        print(fizz_buzz or number)


if __name__ == '__main__':
    run_fizz_buzz(28, {4: 'Argh', 7: 'Blergh'})
