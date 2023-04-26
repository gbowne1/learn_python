# Setback
R = float(input("Enter the bend radius: "))
T = float(input("Enter the metal thickness: "))
SB = R + T
print("The setback distance is:", SB)

# Bend Allowance
import math

radius = float(input("Enter the bend radius: "))
angle = float(input("Enter the bend angle in degrees: "))
thickness = float(input("Enter the metal thickness: "))
k_factor = float(input("Enter the K-factor for this bend: "))

angle_radians = angle * (math.pi / 180)
BA = angle_radians * (radius + k_factor * thickness)

print("The bend allowance is:", BA)

# Bend Deduction 
R = float(input("Enter the desired bend radius: "))
T = float(input("Enter the metal thickness: "))
N = float(input("Enter the number of degrees of bend: "))

BD = (0.0173 * R + 0.0078 * T) * N

print("The bend deduction is:", BD)