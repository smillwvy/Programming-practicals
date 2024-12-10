import math

from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry
def greet():
    name = input("What is your name? ")
    print(f"Hello, {name}!")

def main():
    my_name = input("What is your name? ")
    greet(my_name)
    
def product(a, b):
    return a * b

def divide(a, b):
    return a / b

def divide_and_product(a, b):
    product_result = product(a, b)
    divide_result = divide(a, b)
    return product_result, divide_result

def area_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    return area

def circumference_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    circumference = 2 * math.pi * radius
    return circumference

def circle_info ():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    print("The area of the circle is", area, "and the circumference is", circumference)
    return area, circumference

def draw_block_of_stars(width, height):
    for i in range(height):
        print('*' * width)

def draw_letter_e():
    height = 10
    width = 8
    draw_block_of_stars(width, 2)
    for i in range(2):
        print('*')
    draw_block_of_stars(width, 1)
    for i in range(2):
        print('*')
    draw_block_of_stars(width, 2)

def draw_brown_eye(center_point, radius, win):
    #center = Point(center_point, center_point)
    outer_eye = Circle(center_point, radius)
    outer_eye.fill_colour = "white"
    outer_eye.outline_colour = "black"
    outer_eye.draw(win)
    
    iris_radius = round(radius * 0.6)
    iris = Circle(center_point, iris_radius)
    iris.fill_colour = "brown"
    iris.outline_colour = "black"
    iris.draw(win)
    
    pupil_radius = round(radius * 0.3)
    pupil = Circle(center_point, pupil_radius)
    pupil.fill_colour = "black"
    pupil.draw(win)

def draw_pair_of_brown_eyes():
    win = Window("Pair of Brown Eyes", 400, 200)
    center_point1 = Point(160, 100)
    radius1 = 40
    draw_brown_eye(center_point1, radius1, win)
    
    center_point2 = Point(240, 100)
    radius2 = 40
    draw_brown_eye(center_point2, radius2, win)

    win.get_mouse()
    win.close()





            
        
    
    


    
    
    


    