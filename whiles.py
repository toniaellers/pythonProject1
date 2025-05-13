# while loops exercixe #23
# a. while loops that prints 1-5
#Tonia Ellers

x = 1
while x <6:
   print(x)
   x += 1

print('\n')
print('\n')

# 23 b print 2,5,8,11
x = -1
while x <12:
   print(x + 3)
   x += 3

print('\n')
print('\n')

# 23 c print -10 -8 -6 -4 -2 0
x = -12
while x <0:
   print(x + 2)
   x += 2

print('\n')
print('\n')

from itertools import repeat
def square(string, x):
    for _ in range(x):
        print(''.join(repeat(string, x)))

square("*", 4)
