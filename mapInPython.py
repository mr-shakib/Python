""" map() applies a function to each item in a iterables (list,tuple,set etc)"""

# map(function, iterable)

def cube(x):
    return x*x*x

l = [1,2,3,4,5,6,7,8,9,10]

cubeNum = list(map(cube,l))
for i in cubeNum:
    print(i)


store = [
    ("shirt",20.00),
    ("pant",30.00),
    ("t-shirt",15.00),
    ("shoes",40.00)
]

toEuros = lambda data: (data[0],data[1]*0.82)
toDollars = lambda data: (data[0],data[1]/0.82)

storeEuros = list(map(toEuros,store))
storeDollars = list(map(toDollars,store))


for i in storeEuros:
    print(i)

for i in storeDollars:
    print(i)


