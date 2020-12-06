[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/anthonywritescode/fizzbuzz-intcode/master.svg)](https://results.pre-commit.ci/latest/github/anthonywritescode/fizzbuzz-intcode/master)

fizzbuzz-intcode
================

- https://esolangs.org/wiki/Intcode
- https://adventofcode.com/2019

In particular I am using day 21's implementation of the IntCode computer.  In
this version of the IntCode computer, the output instruction receives
ASCII integers and prints those characters to the screen.

Here's a sample execution of my FizzBuzz program:

```console
$ python3 day21_part1.py fizzbuzz.txt
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, FizzBuzz, 31, 32, Fizz, 34, Buzz, Fizz, 37, 38, Fizz, Buzz, 41, Fizz, 43, 44, FizzBuzz, 46, 47, Fizz, 49, Buzz, Fizz, 52, 53, Fizz, Buzz, 56, Fizz, 58, 59, FizzBuzz, 61, 62, Fizz, 64, Buzz, Fizz, 67, 68, Fizz, Buzz, 71, Fizz, 73, 74, FizzBuzz, 76, 77, Fizz, 79, Buzz, Fizz, 82, 83, Fizz, Buzz, 86, Fizz, 88, 89, FizzBuzz, 91, 92, Fizz, 94, Buzz, Fizz, 97, 98, Fizz, Buzz
```

To see the rough algorithm I used (translated to python) see
[./fizzbuzz.py](./fizzbuzz.py)
