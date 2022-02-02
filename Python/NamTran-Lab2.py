# Python exercise questions
# Help you getting familiar with Python syntax

# Grading:

# IMPORTANT NOTICE:
# A good practice in coding is to show your customer a working version and tell them
# what new features you want to add next.
# Thus, we require you to submit all your homework as a working version. If you
# only know how to solve 7/10 questions, just submit the 7 that runs without errors.
# For incomplete answers, comment the code out and print a line tell us your progress
# E.g. "Problem 3 is a completed but has run time errors"
# or "problem 5 is incomplete, but I did 75% of the work."

# Complete HW + correct results: 10pt
# Each question has a equal share of the total points
# Code that does not run will have only 2pt.
# No submission: 0%

# Please follow the required input/output and function names
# Main function is at the end of the file
# Please call all of your completed functions and print the results out

# Please define all the needed input variables in your main function directly and not asking for
# user input. Also, please format the output from each function and print them out in the main.
import random

'''
 1. Input: Count
 Output: print Count number of "hello":
            1th hello
           2th hello...
 IMPORTANT: copy to visualizer, observe the behavior
'''


def easy_hello_loop1_for(Count):
    i = 0
    while i < Count:
        print("%dth hello\n" % i)
        i += 1


'''
2.Input: number x,y
 Output: return the smaller value of the two
 Do it by yourself, no system calls like min()
'''


def smaller_value(x, y):
    if x < y:
        return x
    else:
        return y


'''
3. Do not use len(). Write a function to calculate how many elements do you have in your list, and return it
'''


def my_len(lis):
    count = 1
    for element in lis:
        count += 1
    return count


'''
4. input: a list with small strings that has 2 letters, 3 letters, or 4 letters
output: return 3 lists, Letter2, Letter3, Letter4 containing small strings. Print results out in the main function.
Sample:
input list: ['rt','asdf','ton','er','user']
will give
    Letter2=['rt','er']
    Letter3=['ton']
    Letter4=['asdf','user']
You can use len() in this question.
'''


def cate_letters(LongStr):
    letter2 = []
    letter3 = []
    letter4 = []
    for element in LongStr:
        if len(element) < 3:
            letter2.append(element)
        elif len(element) < 4:
            letter3.append(element)
        else:
            letter4.append(element)
    print("Letter2=%s" % letter2)
    print("Letter3=%s" % letter3)
    print("Letter4=%s" % letter4)


'''
5. input: a string with letters in it, a string with numbers in it.
We assume they have same amount of characters/length. 
output: go through the two strings together, print out elements by index
format "the elements at index __ from string1 is __, from string2 is ___"
'''


def two_strings1(str1, str2):
    i = 0
    while i < len(str1):
        print("the elements at index %d from string1 is %s, from string2 is %s" % (
            i, str1[i], str2[i]))
        i += 1


'''
6. input: a string with letters in it, a string with numbers in it
output: go through the two strings together. At index i, if the number in str2 is even, put the letter in str1 into evenStr
if the number is odd, put the letter into oddStr. Return the even/odd strings
Sample: "helloworld" "2435232399"
gives evenStr="heoo" oddStr="llwrld"
'''


def two_strings2(str1, str2):
    i = 0
    evenStr = ""
    oddStr = ""
    while i < len(str2):
        if int(str2[i]) % 2 == 0:
            evenStr += str1[i]
        else:
            oddStr += str1[i]
        i += 1
    return evenStr, oddStr


'''
7.
The number 6 is a truly great number. Given two int values, a and b, return True
if either one is 6. Or if their sum or difference is 6.
Note: the function abs(num) computes the absolute value of a number.

love6(6, 4) returns True
love6(4, 5) returns False
love6(1, 5) returns True
'''


def love6(a, b):
    sum = a + b
    difference = a - b
    if a == 6 or b == 6 or abs(sum) == 6 or abs(difference) == 6:
        return True
    return False


'''
########
#8. ISBN number

#As you know, every book has an unique ISBN number (International Standard Book Number).
#It is a 10-digit (or 13) code that uniquely specifies a book. Since this number is long, the right most digit is actually a "checksum"
#to roughly check if all the digits are correct (not mis-typed etc.) and forming a legit ISBN number. (checksum is also used in other places, like credit card number.)
#The rule is: when adding all the (10 numbers * its position (rightmost be position 1, leftmost be 10)) together, the sum should be divisible by 11.
#For example: ISBN 020131452-5 is legit since:
#               (0*10 + 2*9 + 0*8 + 1*7 + 3*6 + 1*5 + 4*4 + 5*3 + 2*2 + 5*1)%11 = 88%11 = 0 the sum 88 is divisible by 11
#In fact, the cool thing is that the checksum (rightmost 5) is the only single digit number that can satisfy this rule. In other words, if you know the first
#9 digit, you can calculate the checksum (last digit). In this problem, you will be calculte the checksum of an ISBN number.
#########
'''
'''
Helper function 1: check_legit_ISBN
Input: a list with 10 single digit number in it
Output: return "Legit" if the 10 digits form a legit ISBN number
        return "Not Legit" otherwise

Sample: [0,2,0,1,3,1,4,5,2,5] should return "Legit"
        [0,2,0,1,3,1,4,5,2,3] should return "Not Legit"

'''


def check_legit_ISBN(ISBNLis):
    sum = 0
    i = len(ISBNLis)
    for number in ISBNLis:
        sum += number * i
        i -= 1
    if sum % 11 == 0:
        return "Legit"
    else:
        return "Not Legit"


'''
Helper func 2: format output
input: a list with 10 numbers in it
output: format it to the correct ISBN format and return it
Sample:
[0,2,0,1,3,1,4,5,2,5] will become: "ISBN 020131452-5"
'''


def format_ISBN(ISBNLis):
    formatted_str = ""
    for number in ISBNLis:
        formatted_str += str(number)
    formatted_str = formatted_str[:9] + "-" + formatted_str[9:]
    return formatted_str


'''
Helper func 3: checksum_ISBN
Input: a list with 9 single digit number in it (first 9 digit in ISBN)
Output: print out: "The correct checksum digit is:__. Now we have a legit ISBN: _____"
Hint: just loop through 0,1,2...X (X represents 10), test every one with helper func1 to find out the one checksum that forms a legit ISBN
with the correct ISBN in lis (10 numbers), call helper func2 to format it correctly. Then print the final result.
(Technical googling practice - google how to append or remove an element from a list)
'''


def checksum_ISBN(partISBN):
    checksum_digit = 0
    ISBN_lis = []
    ISBN = ""
    num = 0
    while num < 11:
        partISBN.append(num)
        if check_legit_ISBN(partISBN) == "Legit":
            checksum_digit = num
            ISBN_lis = partISBN
            ISBN = format_ISBN(ISBN_lis)
        partISBN.pop()
        num += 1
    print("The correct checksum digit is: %d. Now we have a legit ISBN: %s" %
          (checksum_digit, ISBN))


'''
Main Func: Generate a ISBN by:
add 9 random nunmbers into a list
(Technical googling practice - how to generate random numbers?)
call helper func 3 to find the checksum

Repeat 10 times
Generate 10 good ISBN numbers with one function call (not 10 digits for 1 ISBN)
Sample:
The correct checksum digit is:8. Now we have a legit ISBN:123456789-8 
The correct checksum digit is:8. Now we have a legit ISBN:987654321-8 
etc.
'''


def generate_ten_ISBNs():
    num_list = []
    count = 0
    i = 0
    j = 0
    while i < 10:
        while j < 9:
            num_list.append(random.randint(0, 9))
            j += 1
        if j == 9:
            j = 0
        checksum_ISBN(num_list)
        num_list.clear()
        i += 1


if __name__ == '__main__':
    my_list = ['hello', 'world', 'xin', 'chao', 'user']
    my_list1 = ['ab', 'cd', 'cdf', 'arf', 'artg', 'seqd']
    print("****Question 1****")
    easy_hello_loop1_for(5)
    print("****Question 2****")
    print("Smaller value between 4 and 9: ")
    print(smaller_value(4, 9))
    print("****Question 3****")
    print(my_list1)
    print("Length: " + str(my_len(my_list)))
    print("****Question 4****")
    cate_letters(my_list1)
    print("****Question 5****")
    print("abcdef and 012345")
    two_strings1("abcdef", "012345")
    print("****Question 6****")
    odd_str, even_str = two_strings2("abcdef", "012345")
    print("Odd strings:" + odd_str)
    print("Even strings:" + even_str)
    print("****Question 7****")
    print("love6(5,11) return")
    print(love6(5, 11))
    print("love6(3,7) return")
    print(love6(3, 7))
    print("love6(6,8) return")
    print(love6(6, 8))
    print("love6(1,-5) return")
    print(love6(6, 8))
    print("****Question 8****")
    generate_ten_ISBNs()
