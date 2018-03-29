"""
===================   TASK 3   ====================
* Name: Negative and Non-Negative Elements
*
* Write a script that will populate a list with as
* many elements as user defines. For taken number
* of elements the script should take the input from
* user for each element. You should expect that
* user will always provide integer numbers. At the
* end, the script should print how many negative
* and non-negative numbers there were present in
* the list.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

def is_even(number):

    if number % 2 == 0:
        return True
    else:
        return False



list_length = int(input("How many numbers should list have? "))



list_of_numbers = []


for i in range(list_length):
    new_number = int(input("Enter integer number #" + str(i+1) + ": "))
    list_of_numbers.append(new_number)  # Add new number to the list


total_even = total_odd = 0

for number in list_of_numbers:


    if is_even(number):
        total_even += 1
    else:
        total_odd += 1


print("List of numbers: ", str(list_of_numbers))
print("Total even numbers: ", total_even)
print("Total odd numbers: ", total_odd)