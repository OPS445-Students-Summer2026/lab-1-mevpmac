#!/usr/bin/env python3

# Any line that starts with a "#" is also known as a comment,
# these lines are ignored by the python interpreter even if
# they contain code. The very first line is called a Shebang line, 
# it is used to tell the system which interpreter to 
# use(python2, python3, bash, etc). 

#print(10 + 5)    # addition
#print(10 - 5)    # subtraction
#print(10 * 5)    # multiplication
#print(10 / 5)    # division
#print(10 ** 5)   # exponents

#print(5 // 2)    # integer division
#print(5 % 2)     # returns remainder of integer division

#print(10 + 5 * 2)       # multiplication happens before addition
#print((10 + 5) * 2)         # parentheses happen before multiplication
#print(10 + 5 * 2 - 10 ** 2) # first exponents, then multiplication, then addition and subtraction from left-to-right
#print(15 / 3 * 4)       # division and multiplication happen from left-to-right
#print(100 / ((5 + 5) * 2))  # the inner most parentheses are first performing addition, then parentheses again with multiplication, finally the division

x = int(10)
y = int(2)
z = int(5)

product = y * z
sum = x + product

print(f"{x} + {y} * {z} = {sum}")
