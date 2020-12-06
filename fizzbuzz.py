from typing import Tuple


def divmod(n: int, mod: int) -> Tuple[int, int]:
    """implement divison + mod using addition"""
    i = 0
    sub = -1 * mod

    while n >= mod:
        n += sub
        i += 1

    return i, n


def printnum(n: int) -> None:
    # build up a divisor, we'll use this to print one digit at a time
    tens = 10
    while not n < tens:
        tens *= 10
    tens, _ = divmod(tens, 10)

    # print one digit at a time while moving the divisor down
    while tens != 0:
        tmp1, _ = divmod(n, tens)
        _, tmp1 = divmod(tmp1, 10)
        tmp1 += ord('0')
        print(chr(tmp1), end='')

        tens, _ = divmod(tens, 10)


def main() -> int:
    start = 1
    end = 100
    started = 0

    while start <= end:
        if started:
            print(', ', end='')
        started = 1

        _, remainder_3 = divmod(start, 3)
        _, remainder_5 = divmod(start, 5)
        both_non_divisible = remainder_3 * remainder_5

        if remainder_3 == 0:
            print('Fizz', end='')
        if remainder_5 == 0:
            print('Buzz', end='')
        if both_non_divisible:
            printnum(start)

        start += 1

    print('\n', end='')
    return 0


if __name__ == '__main__':
    exit(main())
