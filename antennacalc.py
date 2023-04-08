import math

def dipole():
    frequency = float(input("Enter your frequency in MHZ to calculate a half-wave dipole.\n\n"))
    print("You entered %s MHZ." % frequency)
    length = 468 / frequency
    element = length / 2
    print(f"{round(length, 2)} is the total length of the antenna.")
    print(f"{round(element,1)} feet, is the length of each element.")

dipole()

## Thanks to mattisse for helping me fix this.