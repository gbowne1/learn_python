import math

def dipole():
    frequency = float(input("Enter your frequency in MHZ to calculate a half-wave dipole."'\n''\n'))
    print("You entered %s MHZ."'\n' % frequency)
    length = 468 / frequency
    element = length / 2
    print(float(length, 2), "is the total length of the antenna."'\n')
    print(float(element) 1), "feet, is the length of each element."))
dipole()