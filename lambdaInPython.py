# lambda parameters : expression

def double(x):
    return x * 2
print(double(5))

double = lambda x : x * 2
print(double(5))

multiply = lambda x,y : x * y
print(multiply(5,4))

addNumbers = lambda x,y,z : x+y+z
print(addNumbers(4,5,6))

fullName = lambda firstName,lastName : firstName+ " " +lastName
print(fullName("Mr","Shakib"))

ageCheck = lambda age : True if age >= 18 else False
print(ageCheck(17))
print(ageCheck(28))