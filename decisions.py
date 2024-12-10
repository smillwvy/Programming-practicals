def greet(name):
    print(f"Hello {name}.")
    if len(name) > 20:
        print("That's a long name!")

def can_you_vote(age):
    if age >= 18:
        print("You can vote")
    else:
        print("Sorry, you can't vote")

def get_degree_class(mark):
    if mark >= 70:
        return "1st"
    elif mark >= 60:
        return "2:1"
    elif mark >= 50:
        return "2:2"
    elif mark >= 40:
        return "3rd"
    else:
        return "Fail"

def is_leap_year(year):
    # Not divisible by 4 → Not a leap year
    if year % 4 != 0:
        return False
    # Divisible by 4 but not by 100 → Leap year
    elif year % 100 != 0:
        return True
    # Divisible by 100 but not by 400 → Not a leap year
    elif year % 400 != 0:
        return False
    # Divisible by 400 → Leap year
    else:
        return True

def days_in_month(month, year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 31

def overly_complex_days_in_month(month, year):
    # \ allows the code to continue on the next line
    if month == 1 or month == 3 or month == 5 or month == 7 or \
       month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28

def count_down():
    for i in range(10, 0, -1):
        print(i, "...", end=" ")
    print("Blast Off!")

def meals():
    for day in range(1, 8):
        print(f"Currently on day {day}")
        for meal_number in range(1, 4):
            print(f"- Eating meal {meal_number} of day {day}")
        
def numbered_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()



