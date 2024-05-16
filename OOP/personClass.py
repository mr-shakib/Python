#BASE CLASS

class Person:
    def __init__(self , fname , lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(self.fname , self.lname)
    
person1 = Person("Mr", "Shakib")
person1.printname()

#SUB CLASS
class Student(Person):
    pass

student1 = Student("Mr", "Nacht")
student1.printname()


#SUB CLASS WITH __init__ FUNCTION
class Teacher(Person):
    def __init__(self, fname, lname, age): #if we add __init__ function to a subclass it will not inherit the __init__ class from it's parent class anymore
        self.age = age
        Person.__init__(self, fname, lname) #so we have to make a reference to the parent __init__ function

    def printage(self):
        print(f'Age : {self.age}')

teacher1 = Teacher("Mr", "Karim", 45)
teacher1.printname()
teacher1.printage()

#SUB CLASS WITH super() FUNCTION
class Dropout(Person):
    def __init__(self, fname, lname, year):
        self.year = year
        super().__init__(fname, lname) #super function inherit everything without referencing the parent class __init__ function

    def dropoutyear(self):
        print(f'Dropout Year :{self.year}')

dropout1 = Dropout("Mr", "Idiot", 2020)
dropout1.printname()
dropout1.dropoutyear()

#OVERRIDING sub classes have same methods , parameters, signature
class overRide(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

    def printname(self):
        print(self.lname , self.fname)

override = overRide("Mr", "Overrider")
override.printname()
