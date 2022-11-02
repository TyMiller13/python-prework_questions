# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_"+user_name+"!")

# TEST**
# hello_name("TyMiller")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    max = 100
    for num in range(1, max + 1):
        if (num % 2 != 0):
            print(num)

# TEST**
# first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    max_num = None
    for number in a_list:
        if (max_num is None or number > max_num):
            max_num = number
    print(max_num)

# TEST**
# max_num_in_list([45,22,78,31,13])

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).


def is_leap_year(a_year):
    if (a_year % 4 == 0):
        print(True)
    elif (a_year % 100 == 0 and a_year % 400 == 0):
        print(True)
    else:
        print(False)

# TEST**
# is_leap_year(2024)
# is_leap_year(2030)

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.


def is_consecutive(a_list):
    sorted_a_list = sorted(a_list)
    range_a_list = list(range(min(a_list), max(a_list)+1))
    if sorted_a_list == range_a_list:
        print(True)
    else:
        print(False)

# TEST**
# is_consecutive([2,3,4,5,6,7])
# is_consecutive([1,2,4,5])
# is_consecutive([7,3,5,2,6,4])
# is_consecutive([5,1,2,4])
