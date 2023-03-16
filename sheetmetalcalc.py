# This is a sheet metal usage calculator
# to determine how many parts of a certain size (l x w) be made from
# a certain size (l x w) sheet of metallic material.
# allow for 90deg arrangement of parts

length = input("Input the length of your sheet in inches: ")
width = input("Input the width of your sheet in inches: ")
margin = input("Input the margin width of your sheet in inches: ")
area = int(width) * int(length)
part_len = input("Input the length of your part in inches: ")
part_wid = input("Input the width of your part in inches: ")
part_area = int(part_wid) * int(part_len)
print(f"Your sheet length is {length} inches")
print(f"Your sheet width is {width} inches")

# input: margin {space in inches between part(s)}

print(f"The area of your sheet is {area}.")
print(f"The area your parts cover across your sheet is {part_area} square inches.")
print(f"The number of parts that fit on this sheet width in this configuration is {parts}. ")
print(f"The number of parts that fit on this sheet length in this configuration is {parts}. ")
