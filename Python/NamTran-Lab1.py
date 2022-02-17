# Python lab 1
# Learn from the online interactive tutorial and finish below tasks
# You can edit in this file by filling blanks after each question.
# Submit the .py file for your own reference
# This practice is graded only on submission.
# It will help you to get started on Python for the homework

#####
# Example function
#####
# from pip import main

def example():  # def is function definition
    print("I am the example code")

# Now, go to the end of this file and you will find the main function & how to run your code there
# Around line #94

#####
# 1. function in python
####


def printHello():  # Remove the # at the begining of this line.
    print("Hello World!")
    # tab is IMPORTANT in python. tab in python replaces {} in C++
    # print string hello world. One line of code here. Make sure it is indented to show it belongs to this function

#####
# 2. variable definition in python
#####


def someVars():
    my_interger1 = 4
    my_interger2 = 5
    my_float1 = 3.2
    my_float2 = 4.6
    sum = my_interger1 + my_interger2 + my_float1 + my_float2
    print(sum)
    # define a few integer and float numbers, add them together and print result out

# call the function to run it in the main function at the end of the file

#####
# 3. define a list in python
#####


def mylis():
    # define a list with 5 numbers, print it out
    my_list = [0, 1, 2, 3, 4, 5]
    print(my_list)
    # define an empty list and append a few numbers into it, then print it out
    empty_list = []
    empty_list.append(1)
    empty_list.append(2)
    empty_list.append(3)
    print(empty_list)

# call your mylis func to execute in the main function at the end of the file

#####
# 4. string output
#####


def printstr(user_input_str1, user_input_int1):
    # convert int into string and append the int with the string to form a long string
    # (technical googling practice -- google what func to use)
    converted_int = str(user_input_int1)
    long_string = user_input_str1 + converted_int
    # print the long str out
    print(long_string)

# In the main function, define an user_input string and an user_input int.
# Pass them in as parameters to the function. Call and run the function to see results.

####
# 5. passing var to func and return
####


def funcvars(user_inputvar1, user_inputvar2):
    # add the user_input numbers together
    # returen the result
    return user_inputvar1 + user_inputvar2

# Define the user_input variables in main, pass them into the function.
# In main, use a result variable to receive the result from funcvars and print the result out

####
# 6. for loop
####


def go_over_list(mylis):
    # use for loop to go over the user_input list and print out items one by one
    for item in mylis:
        print(item)


def go_over_list1():
    # use for loop to directly print out numbers from 10 to 17
    for numbers in range(10, 18):
        print(numbers)


def go_over_list2(mylis):
    # use for loop & go over your list
    # multiply 2 to every item in your list, print results out
    for item in mylis:
        print(item * 2)


def go_over_list3(mylis):
    # create an empty list resLis
    res_lis = []
    # go over items in the user_input list, multiply 2 to every item
    # add result one by one to resLis
    for item in mylis:
        res_lis.append(item * 2)
    # return resLis
    return res_lis

# Call all the functions in main. Provide necessary user_inputs to the functions.
# For those with return values, print the return values out in main.

####
# 7. while loop
####


def go_over_list(mylis):
    count = 0
    while count < len(mylis):
        print(mylis[count])
        count += 1


def go_over_list1(mylis):
    count = 10
    while count < 18:
        print(count)
        count += 1


def go_over_list2(mylis):
    count = 0
    while count < len(mylis):
        print(mylis[count] * 2)
        count += 1


def go_over_list3(mylis):
    res_lis = []
    count = 0
    while count < len(mylis):
        res_lis.append(mylis[count] * 2)
        count += 1
    return res_lis

# do all the problems in 6 using while loop instead


#####
# Here is the main function
# You can have only 1 main function in 1 script
# Left click on the green arrow next to the line number of the line of the main function definition
# Your code would run.
if __name__ == "__main__":  # a quick way to type this line is: type "main" and then tab
    print("****Example****")
    example()
    print("****Question 1****")
    printHello()
    print("****Question 2****")
    someVars()
    print("****Question 3****")
    mylis()
    print("****Question 4****")
    str_user_input = "Hello World"
    int_user_input = 123
    printstr(str_user_input, int_user_input)
    print("****Question 5****")
    user_input1 = 30
    user_input2 = 50
    result = funcvars(user_input1, user_input2)
    print(result)
    print("****Question 6****")
    my_list = [1, 2, 3, 4, 5]
    go_over_list(my_list)
    go_over_list1(my_list)
    go_over_list2(my_list)
    print(go_over_list3(my_list))
    print("****Question 7****")
    go_over_list(my_list)
    go_over_list1(my_list)
    go_over_list2(my_list)
    print(go_over_list3(my_list))
    # you can start call and run your functions here

######
# Python is an easier PL to learn than C++ and looks like C++
# From this lab experience, reflect and summary what it feels like
# when you are learning a new PL that is similar to a PL that you already know?
# Your answer here:
# Python is really an easy language to learn compared to C++ or Java since it was close to human language
# I am fluent in Java and C++, thus the first impression of learning Python was too bad. I am exicited to learn more about
# powerful library and other tools

# In this case, when you want to learn a new PL that looks like a PL that you already know,
# how can you learn the new PL quickly? Any steps?
# Your answer here:
# When I learned a PL, I would remember the core structure of the know PL, from that I could learn more about the syntax.
