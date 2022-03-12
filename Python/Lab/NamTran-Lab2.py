import re

def find_int(lis):

    int_reg = re.compile(r"\d+")
    i = 0
    while i < len(lis):
        result = int_reg.match(lis[i])
        if (result != None):
            print(lis[i] + " match a pattern: integer")
            print(result)
            print("\n")
        i += 1

def find_float(lis):

    float_reg = re.compile(r"\d+\.\d+")
    i = 0
    while i < len(lis):
        result = float_reg.match(lis[i])
        if (result != None):
            print(lis[i] + " match a pattern: a float with 1 digit or more")
            print(result)
            print("\n")
        i += 1
def find_exact_float(lis):

    float_exact_reg = re.compile(r"d+\.\d{2}")
    i = 0
    while i < len(lis):
        result = float_exact_reg.match(lis[i])
        if (result != None):
            print(lis[i] + " match a pattern: a float with exactly 2 digit after decimal point")
            print(result)
            print("\n")
        i += 1

def find_float_f(lis):

    float_f_reg = re.compile(r"[-+]?([0-9]*\.[0-9]+|[0-9]+)[f]")
    i = 0
    while i < len(lis):
        result = float_f_reg.match(lis[i])
        if (result != None):
            print(lis[i] + " match a pattern: a float with the letter f")
            print(result)
            print("\n")
        i += 1

def find_mix_word(lis):

    mix_word = re.compile(r"[A-Z]+[a-z]+\d+")
    i = 0
    while i < len(lis):
        result = mix_word.match(lis[i])
        if (result != None):
            print(lis[i] + " match a pattern: word with Capital letters followed by lowercase and digits")
            print(result)
            print("\n")
        i += 1

def find_digits_letters(lis):

    digits_letters = re.compile(r"\d{3}\w+")
    i = 0
    while i < len(lis):
        result = digits_letters.match(lis[i])
        if (result != None):
            print(lis[i] + " match a pattern: exactly three digits followed by at least 2 letters")
            print(result)
            print("\n")
        i += 1

def remove_int(str):
    result = re.search('\d+', str)
    int_part = result.group(0)
    str = str.replace(int_part, "")
    print("Found integer " + int_part + " at the beginning of this string, starting at index  ending at index  The rest of the string is:" + str)

if __name__ == "__main__":
    lis = ['22.11','23','66.7f', '123abcde','Case44', 'Happy','78', '66.7', 'yes123','Book111']
    print("**** TASK 1 ****")
    print("**Finding integer ... \n")
    find_int(lis)
    print("**Finding float consists of 1 or more digits before and after decimal point ...\n")
    find_float(lis)
    print("Finding a float with exactly two digits after decimal pt ... \n")
    find_exact_float(lis)
    print("**Finding float ending with letter f ... \n")
    find_float_f(lis)
    print("**Finding capital letters followed by lower case, followed by digits ... \n")
    find_mix_word(lis)
    print("**Exactly three digits followed by at least 2 letters ... \n")
    find_digits_letters(lis)
    print("*** Task 2 ****")
    remove_int("123  street")
