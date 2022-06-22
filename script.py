"""
Script for running FizzBuzz game.

FizzBuzz game:
1) From 1 to max number, numbers are output
2) If the number is divisible by 3 without remainder, it is replaced by «Fizz»
3) If the number is divisible by 5 without remainder, it is replaced by «Buzz»
4) If the number is divisible by 3 and 5 without remainder,
it is replaced by «FizzBuzz»

Example:
For max number is 16 the output will be:
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16

"""


class FizzBuzzRunner:
    """Run FizzBuzz game and print result"""

    __DEFAULT_REPLACEMENT_OPTIONS = {3: 'Fizz', 5: 'Buzz'}

    def __init__(self, max_number: int, replacement_options=None):
        if not replacement_options:
            replacement_options = self.__DEFAULT_REPLACEMENT_OPTIONS

        self.__max_number = max_number
        self.__replacement_options = replacement_options

    @staticmethod
    def __is_divided_without_remainder(divisible: int, divider: int) -> bool:
        """True if divisible divide to divider without remainder"""

        return divisible % divider == 0

    def __get_string_or_number(self, number: int) -> str | int:
        """Return string (if number divide without remainder) or number"""

        string = ''

        for digit, replacement_string in self.__replacement_options.items():
            if self.__is_divided_without_remainder(number, digit):
                string += replacement_string

        return string or number

    def __print_game_title(self) -> None:
        """Print game's title"""

        print(
            f'\nFizzBuzz with {self.__max_number} limit number and '
            f'{self.__replacement_options} options \n'
        )

    @property
    def __fizz_buzz_values(self) -> tuple:
        """Return result values after FizzBuzz running"""

        values = []

        for number in range(1, self.__max_number + 1):
            values.append(self.__get_string_or_number(number))

        return tuple(values)

    def run(self) -> None:
        """Run game and print results"""

        self.__print_game_title()

        for value in self.__fizz_buzz_values:
            print(value)


if __name__ == '__main__':
    FizzBuzzRunner(16).run()
    FizzBuzzRunner(28, {4: 'Argh', 7: 'Blergh'}).run()
