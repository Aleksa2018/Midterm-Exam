"""
===================   TASK 2   ====================
* Name: Product Of Digits
*
* Write a script that will take an input from user
* as integer number and display product of digits
* for a given number. Consider that user will always
* provide integer number.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""


def product_x(num):
    x=10
    while True:
        print (x)
        y=[int(a) for a in str(x)]
        product = 1
        for z in y:
            product*=z
        if product == num:
            return x
        else:
            x+=1
print(product_x(10))