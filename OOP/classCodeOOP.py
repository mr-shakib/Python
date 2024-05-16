class Person:
    def __init__(self):
        self.name = "Default Name"
        self.age = 20

# Creating an instance of Person
person1 = Person()

print(person1.name)  # Output: Default Name
print(person1.age)   # Output: 20



#########################



class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    


p1 = Person("Daffodil", 20)

print(p1.name)
print(p1.age)




#####################


class Person:
    pass

person1 = Person()

# Dynamically adding attributes to person1
person1.name = "Alice"
person1.age = 30

print(person1.name, person1.age)





###################

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age


    def running(self):
        print(f'hey i am {self.name}, now i am running!')

    def ageCall(self):
        print(f'hey my age is {self.age}')


p1 = Person("Daffodil", 20)

print(p1.name)
print(p1.age)
p1.running()
p1.ageCall()


#############################



class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.__private_attribute = 42  # Private attribute


    def running(self):
        print(f'hey i am {self.name}, now i am running!')

    def ageCall(self):
        print(f'hey my age is {self.age}')

    def get_private_attribute(self):
        return self.__private_attribute

    def set_private_attribute(self, value):
        self.__private_attribute = value


p1 = Person("Daffodil", 20)

print(p1.name)
print(p1.age)
p1.running()
p1.ageCall()

#### print(obj.__private_attribute) #### ERROR
print(p1.get_private_attribute())  # Output: 42
p1.set_private_attribute(100)
print(p1.get_private_attribute())




################################




class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.__private_attribute = 42  # Private attribute
        self._protected_attribute = 70 # Protected attribute


    def running(self):
        print(f'hey i am {self.name}, now i am running!')

    def ageCall(self):
        print(f'hey my age is {self.age}')

    def get_private_attribute(self):
        return self.__private_attribute

    def set_private_attribute(self, value):
        self.__private_attribute = value

    def _protected_method(self):
        print("This is a protected method")


p1 = Person("Daffodil", 20)

print(p1.name)
print(p1.age)
p1.running()
p1.ageCall()

#### print(obj.__private_attribute) #### ERROR
# python does this by name mangling. Instead of hiding the attributes 
# it actually changes the name so that user cannot predict the names. 
# it actually doesn't make it truly private like in java 
print(p1.get_private_attribute())  # Output: 42
p1.set_private_attribute(100)
print(p1.get_private_attribute())

# This is a way to signal developers to now work with protected variables outside class. 
print(p1._protected_attribute)  # Output: 42
p1._protected_method()          # Output: This is a protected method






###########################




class Ball():
    def __init__(self):
        print(f'Ball Created')

    def who_am_i(self):
        print(f'I am a ball')


class SecondBall(Ball):
    def __init__(self):
        print(f'Second Ball Created')

    def who_am_i_ball(self):
        print(f'I am a second ball')


class Football(SecondBall):
    def __init__(self):
        Ball.__init__(self) # call parent class constructor
        super().__init__()
        print(f'football Creaed!')



myFootBall = Football()
myFootBall.who_am_i()




#################################


class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating an instance of Dog
dog = Dog()

# Accessing methods from the parent class
dog.sound()  # Output: Animal makes a sound
dog.bark()   # Output: Dog barks



################## Single Inheritance

class Parent:
    pass

class Child(Parent):
    pass


###############    Multiple Inheritance


class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass
	
######################  Multilevel Inheritance


class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass








#########################     Hierarchical Inheritance


class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass


################# Hybrid Inheritance


class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass

class Grandchild(Child1, Child2):
    pass



##############################


class Parent1:
    def __init__(self):
        self.age = 10

class Parent2:
    def __init__(self):
        self.age = 100

class Child(Parent1, Parent2):
    pass

c = Child()
print(c.age)

########################


class Parent1:
    def __init__(self):
        self.age = 10

class Parent2:
    def __init__(self):
        self.age = 100

class Child(Parent2, Parent1 ):
    pass

c = Child()
print(c.age)
print(Child.mro())


###################

class Cat:
    def sound(self, name):
        self.name = name
        print(f'{self.name} sound Meow!')

class Dog:
    def sound(self, name):
        self.name = name
        print(f'{self.name} sound Woof Woof!!!')

cat = Cat()
dog = Dog()
cat.sound('Kitty')
dog.sound('Doggy')



###################



class Animal:
    def sound(self):
        print(f'sound Animal!!!')

class Dog(Animal):
    def sound(self):
        print(f'sound Woof Woof!!!')

cat = Animal()
dog = Dog()
cat.sound()
dog.sound()


########################

class Animal:
    def sound(self):
        print(f'sound Animal!!!')

class Dog(Animal):
    pass

cat = Animal()
dog = Dog()
cat.sound()
dog.sound()





###########################


try:
    x = 10 / 0  # ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero occurred")




###########################


try:
    age = int(input("Enter your age: "))
    result = 10 / age
except ValueError:
    print("Error: Please enter a valid integer")
except ZeroDivisionError:
    print("Error: Division by zero occurred")
	
	

################################### The else block is executed if no exceptions occur in the try block. It is optional and
 ####is typically used for code that should run only if the try block does not raise any exceptions.


try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero occurred")
else:
    print("Result:", result)




############################


try:

    div = 10/1

except:
    print('Dividing incorrectly')
else:
    print("Division done correctly")
finally:
    print('I dont care')


########################


try:
    file = open("example.txt", "r")
    # Perform operations on the file
except FileNotFoundError:
    print("Error: File not found")
finally:
    # Close the file, regardless of exceptions
    file.close()

print('hello')



##################################


file = None
try:
    file = open("example.txt", "r")
    # Perform operations on the file
except Exception:
    print("Error: File not found")
finally:
    # Close the file, regardless of exceptions
    try:
        file.close()
    except Exception:
        print("error")


print('hello')


#

ValueError
ZeroDivisionError
IndexError
KeyError
PermissionError
FileNotFoundError
ArithmeticError





