# This is a sheet metal usage calculator
# to determine how many parts of a certain size (l x w) be made from
# a certain size (l x w) sheet of metallic material.
# allow for 90deg arrangement of parts

import math


length = int(input("Input the length of your sheet in inches: "))
width = int(input("Input the width of your sheet in inches: "))

margin = int(input("Input the margin width of your sheet in inches: "))

part_len = int(input("Input the length of your part in inches: "))
part_wid = int(input("Input the width of your part in inches: "))


area_big = length * width
area_little = part_len * part_wid
print(f"The area of your sheet is {area_big}.")
print(f"The area your parts cover across your sheet is {area_little} square inches.")



area_big = (length - 2 * margin / 2) * (width - 2 * margin / 2)
area_little = (part_len + margin / 2) * (part_wid + margin / 2)

parts = math.floor(area_big / area_little)

print(f"{parts} pieces can be cut from the sheet. ")
print(f"The area your parts cover across your sheet is {parts * (part_len * part_wid)} square inches.")
print(f"The number of parts that fit on this sheet length in this configuration is {math.floor((length - margin) / (part_len + margin / 2))}. ")
print(f"The number of parts that fit on this sheet width in this configuration is {math.floor((width - margin) / (part_wid + margin / 2))}. ")
