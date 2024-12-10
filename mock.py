import math
def biscuit_cutting():
    diameter_of_biscuit = float(input("Enter diameter of each biscuit in cm : "))
    number_of_biscuits = int(input("Enter the number of biscuits: "))
    length_of_mixture = float(input("Enter the length of the mixture: "))
    width_of_mixture = float(input("Enter the width of the mixture: "))
    
    radius = diameter_of_biscuit / 2
    print("The radius of a biscuit is", radius, "cm")
    
    area = math.pi * (radius ** 2)
    print("The area of a biscuit is", area, "cm")
    
    spare = (length_of_mixture * width_of_mixture) - area

    total_area = length_of_mixture * width_of_mixture
    print("The total area of a biscuit mixture is", area, "cm" )
    
    
    
    
    
    
  
    
    

    
    