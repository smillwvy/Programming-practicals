def say_name():
    print("Amaliia")
    
def say_hello_2():
    print("hello")
    print("world")
          
def dollars_to_pounds():
    dollars = float(input("Enter amount of money in dollars:"))
    pounds = dollars/1.35
    print("The amount of money in pounds is", pounds)
    
def sum_and_difference():
    first = float(input("Enter your 1st number:"))
    second = float(input("Enter your 2nd number:"))
    print(f"Sum is {first + second}")
    print(f"Difference is {first - second}")
 
def change_counter():
    one_pence = int(input("Enter how many 1p coins do you have:"))
    two_pence = int(input("Enter how many 2p coins do you have:"))
    five_pence = int(input("Enter how many 5p coins do you have:"))
    total = one_pence + two_pence * 2 + five_pence *5 
    print("The total amount of money in pence is", total)
    
def ten_hellos():
     for number in range (10):
        print("Hello World")
        
def zoom_zoom():  
    number = int(input("Enter a number of zoom outputs:"))
    for number in range (1, number + 1):
        print("zoom", number )
        
def count_to():
    number = int(input("Enter the number to be counted:"))
    for i in range (number):
        print(i+1)

def count_from_to():
    first_number = int(input("Enter the number to be counted:"))
    second_number = int(input("Enter the number to be counted:"))
    for i in range (first_number, second_number + 1):
        print(i)
        
def weights_table():
    kilogram = int(input("Enter weight in kilograms:"))
    
    
  




    
 
    