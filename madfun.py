#Tonia Ellers
#Program takes User inputs and converts to absolute value, rounded to next whole number
# and calculates sq rt

import math
from math import sqrt

absolute = float(input("Enter 8.88: ")
print(absolute)

rounded = math.ceil(absolute)
print(f"{rounded:.1f}")

square = math.sqrt(rounded)
absolute_value = abs(square)
print(f"{square:.2f}\n")


debit = float(input("Enter -24.75: "))
absolute_value = abs(debit)
print(absolute_value)

rounded = round(debit)
print(f"{rounded:.1f}")

square = math.sqrt(absolute_value)
absolute_value = round(abs(square))
print(f"{square:.1f}")
