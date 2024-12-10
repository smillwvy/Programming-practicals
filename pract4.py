#from github
import os

def student_info():
    course = input("What's your course? ")
    student_id = input("What's your ID number? ")
    print("Welcome to:\t" + course)
    print("\n" * 2 + "Your ID number is:\t" + student_id[2:])


def personal_details():
    name = input("What's your name? ")
    age = int(input("What's your age? "))
    height = float(input("What's your height? "))
    # print("name:\t{:>10}\nage:\t{:>10}\nheight:\t{:>10.2f}".format(name, age, height))
    print(f"name:\t{name:>10}\nage:\t{age:>10}\nheight:\t{height:>10.2f}")


def read_quote():
    print("Current directory:\t" + os.getcwd())
    print("Files in current directory:\t" + str(os.listdir()))
    # Change directory to the folder containing quotation.txt
    os.chdir("text_files")
    # Checking if quotation.txt is in the current directory:
    print("Current directory:\t" + os.getcwd())
    print("Files in current directory:\t" + str(os.listdir()))

    input_file = open("quotation.txt", "r")

    content = input_file.read()
    print(content)


def write_quote():
    os.chdir("text_files")
    output_file = open("my_quotation.txt", "w")

    # You can use `write()` to write a single string
    print("I love Python!", file=output_file)
    print("(Matthew Poole)", file=output_file)

    # Or write both lines in one go separated by a newline character ('\n')
    # content = "I love Python!\n(Matthew Poole)"
    # output_file.write(content)

#from github
    
#Exercise 1
def personal_greeting():
    name = input("Please enter your name: ")
    greeting = "Hello " + name + ", nice to see you!"
    
    print(greeting)

#Exercise 2
def formal_name():
    given_name = input("Please enter your given name: ")
    family_name = input("Please enter your family name: ")
    formal_version = given_name[0] + ". " + family_name
    
    print(formal_version)

#Exercise 3
def kilos_to_ounces():
    kilos = float(input("Enter the weight in kilos: "))
    ounces = kilos * 35.274
    kilos_rounded = round(kilos, 2)
    ounces_rounded = round(ounces, 2)
    
    output_message = str(kilos_rounded) + " kilos is equal to " + str(ounces_rounded) + " ounces"
    
    print(output_message)
    
#Exercise 4
def generate_email():
    forename = input("Enter your forename: ")
    surname = input("Enter your surname: ")
    entry_year = input("Enter the year you entered the university: ")

    # get first four letters of the surname, convert to lowercase
    email_username = surname[:4].lower()
    
    # get first letter of the forename, convert to lowercase
    email_username += '.' + forename[0].lower()

    # get last two digits of the entry year
    email_username += '.' + entry_year[-2:]

    email_address = email_username + '@myport.ac.uk'

    print(email_address)

#Exercise 5
def sing_a_song():
    word = input("Enter the word for the song: ")
    lines = int(input("Enter the number of lines: "))
    repeats = int(input("Enter how many times to repeat the word: "))
    
    for i in range(lines):
        print((word + " ") * repeats)
        
#Exercise 10
def file_in_caps():
    filename = input("Enter the name of the file: ")
    file = open(filename, "r")
    contents = file.read()
    print(contents.upper())
    
    file.close()


    
