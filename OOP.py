# object oriented programming
class person:
    def __init__(self,name,age):
        # this is a constructor method
        # it takes 2 parameters and initialize it as attribute
        self.name = name
        self.age = age
    def myfunctions(self):
        print(f"Hello my name is {self.name} and my age is {self.age}")
        # this is a method function
# create an object or an instance of a class
myobj=person("John",20)
myobj.myfunctions()
myobj2=person("Quavo huncho",33)
myobj2.myfunctions()
myobj3=person("Henya",18)
myobj3.myfunctions()
myobj4=person("Allian",24)
myobj4.myfunctions()
myobj5=person("Castro Fidel",90)