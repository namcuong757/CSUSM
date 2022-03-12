'''
BNF for var def code with format:

myvar= 5+6+2.3;

BNF: 

exp -> id = math;
math -> int+math | float

Note that this is just a shortened example code for demostration only. The final tree misses internal nodes like int or float, since we are not doing word level BNF here.
'''


'''
Task 1: This algorithm will NOT be able to process the string myvar=2*3*4*2.3
because this string does not contain a plus sign. It will be able to process strings
like "myVar=2.25 + 5.5" or "myVar=5+8*6.6"

Task 2:
Exp -> keyword id=math
math -> multi + multi
multi -> int*multi | float

Task 3: 
The string "float myVar=2.4+5*6.1+3.5" would NOT process because it has an extra
addition step that is not included in our BNF grammar. It could process the following:
"float myFloat=2.7+5*6.7" "float myFloat=3*2.7+9*2.7"



'''

inToken = ("empty", "empty")


def accept_token(Mytokens):
    global inToken
    print("     accept token from the list:"+inToken[1])
    inToken = Mytokens.pop(0)


def multi(Mytokens):
    print("\n----parent node mulity, finding children nodes:")
    global inToken
    if(inToken[0] == "float"):
        print("child node (internal): float")
        print("   multi has child node (token):"+inToken[1])
        accept_token(Mytokens)
    elif (inToken[0] == "int"):
        print("child node (internal): int")
        print("   multi has child node (token):"+inToken[1])
        accept_token(Mytokens)

        if(inToken[1] == "*"):
            print("child node (token):"+inToken[1])
            accept_token(Mytokens)

            print("child node (internal): multi")
            multi(Mytokens)
        else:
            print("error, you need * after the int in the math")

    else:
        print("error, multi expects float or int")

def math( Mytokens):
    print("\n----parent node math, finding children nodes:")
    global inToken
    multi(Mytokens)
    if(inToken[1] == "+"):
         print("child node (token) of Math:"+inToken[1])
         accept_token(Mytokens)
    multi(Mytokens)

def exp(Mytokens):
    print("\n----parent node exp, finding children nodes:")
    global inToken
    typeT, token = inToken
    if(typeT == "key"):
        print("child node (internal): keyword")
        print("   keyword has child node (token):"+token)
        accept_token(Mytokens)
    else:
        print("expect identifier as the first element of the expression!\n")
        return
    if(inToken[0] == "id"):
        print("child node (internal): identifier")
        print("   identifier has child node (token):"+inToken[1])
        accept_token(Mytokens)
    else:
        print("expect identifier as the second element of the expression!\n")
        return

    if(inToken[1] == "="):
        print("child node (token):"+inToken[1])
        accept_token(Mytokens)
    else:
        print("expect = as the second element of the expression!")
        return

    print("Child node (internal): math")
    math(Mytokens)


def main():
    global inToken
    Mytokens = [("key", "float"), ("id", "mathresult1"), ("op", "="), ("int", "5"), ("op", "*"),
     ("float", "4.3"), ("op", "+"), ("float", "2.1"), ("sep", ";")]
    inToken = Mytokens.pop(0)
    exp(Mytokens)
    if(inToken[1] == ";"):
        print("\nparse tree building success!")
    return


main()
