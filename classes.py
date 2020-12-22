# Class ile çalışmak
# self class'ın referansına denk gelir
# __init__ OOP ile çalışırken nesne hafızada yer aldığında çalışacak ilk kod

class Math:
    def addition(self, number1,number2):
        return number1 + number2

    def extraction (self, number1,number2):
        return number1 - number2

    def multiplication (self, number1,number2):
        return number1 * number2

    def division (self, number1,number2):
        return number1 / number2 

math = Math()
print("division =" + str(math.division(50,5)))                   


class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName  = lastName
        self.age       = age

person1 = Person("Ellie","John",20)
print(person1.firstName)        

class Worker(Person): 
    def __init__(self,salary):
        self.salary = salary