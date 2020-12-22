def addition (number1,number2):
    return number1 + number2

def extraction (number1,number2):
    return number1 - number2 

def division (number1,number2):
    return number1 / number2 

def multiplication (number1,number2):
    return number1 * number2          

print("Select your operation")
print("1 : Addition")
print("2 : Extraction")
print("3 : Division")
print("4 : Multiplication")

option = input("Select Your OPeration:")

number1 = int(input("Enter your first number:"))
number2 = int(input("Enter your second number:"))

if option == '1':
    print("Addition : " +str(addition(number1,number2)))
elif option == '2':
    print("Extraction : " +str(extraction(number1,number2)))
elif option == '3':
    print("Division : " +str(division(number1,number2)))
elif option == '4':
    print("Multiplication : " +str(multiplication(number1,number2)))
else:
    print("Invalid Transaction")            

