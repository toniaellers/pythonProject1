# 7. Write a function there that takes a number n as a parameter, and returns 2n if n is positive,
# and 0 otherwise. Your function should ouput the following for the given calls:
#there(5)  32
#there(0)  1
#there(3)  8
#there(-2) 0
#there(-6) 0
#print("there(5)", there(5) ==32)
#print("there(0)", there(0) ==1)
#print("there(3)", there(3) ==8)
#print("there(-2)", there(-2) ==0)
#print("there(-6)", there(-6) ==0)

def main():

def there(n):
    if n > 0:
        return 2 * n
    else:
        return 0
main()
