print("Hello World")
def say_hello():
    print("Hello World")

def say_bye():
    print("Goodbye Mars")
    
# A simple kilograms to ounces conversion program
# It asks for a weight in kilograms (for example 10)
# and converts it to ounces (352.74)
    
def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms:"))
    ounces = 35.274*kilos
    print("The weight in ounces is", ounces)
          
def count():
    for number in range (10):
        print("Number is now: ", number)