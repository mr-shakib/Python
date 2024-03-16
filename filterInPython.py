""" filter() = creates a collection of element from an iterable for which a function returns true"""

# filter(function, iterable)


def num(x):
    return x>=5

l = [1,2,3,4,5,6,7,8,9,10]

greaterNum = list(filter(num,l))
for i in greaterNum:
    print(i)


agents_and_ages = [
    ("Jett", 23),
    ("Reyna", 21),
    ("Cypher", 28),
    ("Omen", 145),
    ("Brimstone", 50),
    ("Killjoy", 23),
    ]

age = lambda data: data[1]>=25

drink = list(filter(age,agents_and_ages))
for i in drink:
    print(i)
