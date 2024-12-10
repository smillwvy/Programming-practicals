from graphix import Window, Circle, Point
from time import sleep

def add_up_numbers1():
    total = 0
    more = "y"
    while more == "y": # The loop runs while `more` is "y"
        number = int(input("Enter a number: "))
        total = total + number
        more = input("Any more numbers? (y/n) ")
    print("The total is", total)

def add_up_numbers2():
    total = 0
    number = int(input("Number (0 to stop): "))
    while number != 0: # The loop runs while `number` is not 0
        total = total + number
        number = int(input("Number (0 to stop): "))
    print("The total is", total)

def add_up_numbers3():
    total = 0
    n_str = input("Number (hit enter to stop): ")
    while n_str != "": # n_str is a variable that holds the user input as a string # The loop runs while `n_str` is not empty
        number = int(n_str) # Assumes that `n_str` contains a number
        total = total + number
        n_str = input("Number (hit enter to stop): ")
    print("The total is", total)

def add_up_numbers4():
    total = 0
    while True: # The loop runs until we break it
        n_str = input("Number (anything else to stop): ")
        if not n_str.isdigit():
            break # Break the loop if `n_str` is not a number
        number = int(n_str)
        total = total + number
    print("The total is", total)
    
def can_apply_for_job(degree, experience):
    if (degree == "1st" or degree == "2:1") and experience >= 1:
        return True
    elif degree == "2:2" and experience >= 2:
        return True
    else:
        return False

def get_positive_number1():
    number = 0
    while number <= 0:
        number = int(input("Enter a positive number: "))
    return number

def get_positive_number2():
    while True: #infinite loop
        number = int(input("Enter a positive number: "))
        if number > 0:
            break #This means that the loop will continue running forever unless stopped using a break statement.
    return number

#Exercise 1
def get_name():
    while True:
        name = input("Please enter your name: ")
        if name.isalpha():
            return name
        else:
            print("Error! Please enter a name with alphabetic characters.")

#Exercise 2
def traffic_lights():
    win = Window("Traffic Lights", 400, 400)
    
    red = Circle(Point(100, 50), 20)
    red.fill_colour = "red"
    red.draw(win)
    
    amber = Circle(Point(100, 100), 20)
    amber.fill_colour = "black"
    amber.draw(win)
    
    green = Circle(Point(100, 150), 20)
    green.fill_colour = "black"
    green.draw(win)
    
    while True:
        red.fill_colour = "red"
        amber.fill_colour = "black"
        green.fill_colour = "black"
        sleep(5)
        
        red.fill_colour = "red"
        amber.fill_colour = "yellow"
        green.fill_colour = "black"
        sleep(2)
        
        red.fill_colour = "black"
        amber.fill_colour = "black"
        green.fill_colour = "green"
        sleep(5)

#Exercise 3
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

def grade_coursework():
    while True:
            mark = int(input("Enter a mark between 0 and 20: "))
            if 0 <= mark <= 20:
                grade = calculate_grade(mark)
                print("The grade is:", grade)
                break
            else:
                print("Incorrect mark! Please enter a mark between 0 and 20.")






