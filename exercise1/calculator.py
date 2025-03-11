# Exercise 1: Basic Calculator Functions
from typing import Union

# Defining a Number type for cleaner type hints
Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    print('The sum of a and b is ',a+b)
    pass


def subtract(a: Number, b: Number) -> Number:
    print('The subtract of a and b is ',a-b)
    pass


def multiply(a: Number, b: Number) -> Number:
     print('The product of a and b is ',a*b)
     pass


def divide(a: Number, b: Number) -> Number:
    if b==0:
        raise ValueError("Attempted to divide by Zero.")
    else:
        return a/b
    pass    pass


