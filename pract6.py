import math

def fast_food_order_price():
    basic_price = float(input("Enter the basic price of your order: £"))
    delivery_charge = 0
    if basic_price < 20:
        delivery_charge = 2.50
    total_price = basic_price + delivery_charge
    print("The total price of your order is £", total_price)
    
def what_to_do_today():
    temperature = float(input("Enter today's temperature: "))
    if temperature > 25:
        print("Go for a swim in the sea!")
    elif temperature >= 10:
        print("Go shopping in Gunwharf Quays!")
    else:
        print("Watch a film at home!")
        
def display_square_roots(start, end):
    for number in range(start, end + 1):
        print(f"The square root of {number} is {number ** 0.5:.3f}")

def calculate_grade(mark):
    if mark < 0 or mark > 20:
        return "X"
    elif mark >= 16:
        return "A"
    elif mark >= 12:
        return "B"
    elif mark >= 8:
        return "C"
    else:
        return "F"

from graphix import Window, Circle, Point
def peas_in_a_pod():
    number_of_peas = int(input("Enter the number of peas: "))
    win = Window("Peas in a Pod", 100 + number_of_peas * 100, 100)
    for i in range(number_of_peas):
        x_position = 50 + i * 100
        y_position = win.height // 2
        center_point = Point(x_position, y_position)
        pea = Circle(center_point, 50)
        pea.fill_colour = "green"
        pea.draw(win)
        
    win.get_mouse()
    win.close()
    
def ticket_price(distance, age):
    base_price = 10
    cost_per_km = 0.15
    full_price = base_price + distance * cost_per_km
    if age <= 15 or age >= 60:
        discounted_price = full_price * 0.60
        return discounted_price
    else:
        return full_price

def numbered_square(n):
    number = 1
    for i in range(n):
        for j in range(n):
            print(number, end=" ")
            number += 1 #the same as number = number + 1
        print()

def eye_picker():
    win = Window("Eye Picker", 400, 400)
    x = int(input("Enter the x-coordinate of the eye center (0 to 400): "))
    y = int(input("Enter the y-coordinate of the eye center (0 to 400): "))
    radius = int(input("Enter the radius of the eye: "))
    colour = input("Enter the eye colour (blue, grey, green or brown): ").lower()
    
    if 0 <= x <= 400 and 0 <= y <= 400:
        
        if colour in ["blue", "grey", "green", "brown"]:
            center_point = Point(x, y)
            eye = Circle(center_point, radius)
            eye.fill_colour = colour
            eye.outline_colour = "black"
            eye.draw(win)
        else:
            print("Not a valid eye colour")
    else:
        print("Eye centre not in window")
        
    win.get_mouse()
    win.close()

def draw_coloured_eye(center_point, radius, colour, win):
    eye = Circle(center_point, radius)
    eye.fill_colour = colour
    eye.outline_colour = "black"
    eye.draw(win)

def eyes_all_around():
    win = Window("Eyes All Around", 500, 500)
    eye_colours = ["blue", "grey", "green", "brown"]
    radius = 30
    
    for i in range(30):
        click_position = win.get_mouse()
        colour = eye_colours[i % 4]
        draw_coloured_eye(click_position, radius, colour, win)
        
    win.get_mouse()
    win.close()

