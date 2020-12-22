## Faktöriyel hesaplama
number = int(input("Enter the number : "))

factorial = 1

if number<0:
    print("Negative numbers have no factorial!")

elif number==0:
    print("Result : 1")

else:
    for i in range(1, number+1):
        factorial = factorial * i
    print("Result : ", factorial)            
