import math
def speed_calculator():
    distance = int(input("Enter the distance travelled in kilometers: "))
    duration = int(input("Enter the duration of the journey in hours: "))
    speed = distance / duration
    print("The average speed is", speed, "km/h")

def circumference_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    circumference = 2 * math.pi * radius
    print("The circumference of the circle is", circumference)

def area_of_circle():
   radius = float(input("Enter the radius of the circle: "))
   area = math.pi * (radius ** 2)
   print("The area of the circle is", area)
  
def cost_of_pizza():
    diameter = float(input("Enter the diameter of the pizza in cm: "))
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    cost_in_pence = area * 3.5
    cost_in_pounds = cost_in_pence / 100
    print("The cost of the pizza is £", cost_in_pounds)

def slope_of_line():
    x_1 = float(input("Enter x1: "))
    y_1 = float(input("Enter y1: "))
    x_2 = float(input("Enter x2: "))
    y_2 = float(input("Enter y2: "))
    slope = y_2-y_1/x_2-x_1
    print("The slope of the line is", slope)
    
def distance_between_points():
    x_1 = float(input("Enter x1: "))
    y_1 = float(input("Enter y1: "))
    x_2 = float(input("Enter x2: "))
    y_2 = float(input("Enter y2: "))
    distance = ((x_2 - x_1)**2 + (y_2 - y_1)**2)**1/2
    print("The distance between points is", distance)

def travel_statistics():
    average_speed = float(input("Enter the average speed of a vehicle in km/hour: "))
    duration = float(input("Enter the duration of the journey in hours: "))
    distance = average_speed * duration
    print("The distance is", distance, "km")
    fuel = distance * 5
    print("The amount of fuel used is", fuel, "litre")
    
def sum_of_square():
    number = int(input("Enter the number: "))
    sum_of_numbers = 0
    for i in range (1, n + 1):
        sum_of_numbers += i**2
    print(sum_of_numbers)
    
def average_of_numbers():
     number = int(input("How many numbers there are to be inputted: "))
     average = number/2
     print("The average of numbers is", average)


 




