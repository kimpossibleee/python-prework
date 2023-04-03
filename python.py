'''
Question 1
Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):
'''
def hello_name(user_name):
    print(f"hello_{user_name}")

'''
Question 2
Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
'''
def first_odds():
    for num in range(1, 101):
        if num % 2 is not 0:
            print(num)
    return

'''
Question 3
Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):
'''
def max_num_in_list(a_list):
    return max(a_list)

'''
Question 4
Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):
'''
def is_leap_year(a_year: int):
    if a_year % 4 != 0:
        return False
    else:
        if a_year % 100 == 0:
            return (a_year % 400 == 0)
        return True

'''
Question 5

Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):
'''
def is_consecutive(a_list):
    sorted_list = sorted(a_list)
    first = sorted_list[0]
    for i in range(1, len(sorted_list)):
        if first + 1 != sorted_list[i]:
            return False
        first = sorted_list[i]
    return True



# TESTCASES!!!

a_list = [0, 4, 16, 19, 25, 4, 5]
list1 = [2,3,4,5,6,7]
list2 = [1,2,4,5]

# Question 1:
hello_name("Christina")

# Question 2:
first_odds()

# Question 3:
print(max_num_in_list(a_list))

# Question 4:
print(is_leap_year(2024))

# Question 5:
print(is_consecutive(list1))
print(is_consecutive(list2))
