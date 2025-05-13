# Write a function, pyramid, that takes a single character and a number as parameters and
# displays an ASCII art pyramid to the screen with number rows:
# Tonia Ellers

def pyramid(char, n):
    for i in range(1, n + 1):
        print(char * i)
def main():
    pyramid("*", 2)
    print()
    pyramid("+", 5)
    print()
    pyramid("x", 10)
main()