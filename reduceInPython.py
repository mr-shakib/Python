""" reduce() = apply a function to an iterable and reduce it to a single cumilative value"""

# reduce(function, iterable)

from functools import reduce


def sumf(x, y):
    return x + y

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

summation = reduce(sumf, l)
print(summation)

letters = ["H", "E", "L", "L", "O"]
word = reduce(lambda x,y: x+y,letters)
print(word)

fact = [5,4,3,2,1]
factorial = reduce(lambda x,y: x*y, fact)
print(factorial)
