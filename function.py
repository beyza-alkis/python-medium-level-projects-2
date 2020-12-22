##city = "Tokyo"
##print(city.upper())
##print(city.endswith("o"))
## .upper büyük harflere dönüştürür
## .endswith belirlediğimiz harfle bitip bitmediğini bize 'true' ya da 'false' ile gösterir.


def welcome(name):
    print("Hello " + name)
welcome("Beyza")

def goodBye(name = "butterfly"):
    print("Hello " + name)
goodBye("butterfly")       


def calculateRightTriangle(a,b):
    return a*b/2

area = calculateRightTriangle(2,3)    
print(area)

## Lambda fonksiyonu
calculateAreaRectangle = lambda a,b : a*b
print(calculateAreaRectangle(4,5))