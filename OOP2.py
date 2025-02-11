# Using oop create a class called cars that have the following attributes model,color, and year of manufacture .Implement constructor method and a method function that prints
# (My favourite cars is It is this in colour and manufactured in which year) create instance of that class
class cars:
    def __init__(self,color,model,yearofmanufacture):
        self.color=color
        self.model=model
        self.yearofmanufacture=yearofmanufacture
    def describe(self):
        print(f"My favourite car is {self.model}.It is {self.color} in color and manufactured on {self.yearofmanufacture}")

mycar=cars("green","Mercedes",2006)
mycar.describe()
mycar2=cars("Purple","Lamborghini",2021)
mycar2.describe()
mycar3=cars("White","rolls royce",1998)
mycar3.describe()
mycar4=cars("Red","Porshe",2016)
mycar4.describe()
mycar5=cars("Blue","BMW",1976)
mycar5.describe()