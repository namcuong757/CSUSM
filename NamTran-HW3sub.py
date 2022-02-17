import re


def cutonelinetokens(string):
    result = []
    while(string):
        keyw_reg = re.compile(r"(\bif\b)|(\belse\b)|(\bfloat\b)|(\bint\b)")
        ope_reg = re.compile(r"\+|\*|=|>")
        sep_reg = re.compile(r"\(|\)|:|\"|;")
        id_reg = re.compile(r"([A-Za-z]+\d+)|([A-Za-z]+)")
        int_reg = re.compile(r"(?<![\d.])[0-9]+(?![\d.])")
        float_reg = re.compile(r"\d+\.\d+")
        string_reg = re.compile(r'[A-Za-z]+')

        keyw_token = keyw_reg.match(string)
        ope_token = ope_reg.match(string)
        sep_token = sep_reg.match(string)
        id_token = id_reg.match(string)
        int_token = int_reg.match(string)
        float_token = float_reg.match(string)
        string_token = string_reg.match(string)
        # keyword
        if(keyw_token != None):
            new_string = "<key, " + keyw_token.group(0) + ">"
            result.append(new_string)
            string = string.replace(keyw_token.group(0), ' ', 1)
            string = string.lstrip()
        # operator
        elif(ope_token != None):
            new_string1 = "<op, " + ope_token.group(0) + ">"
            result.append(new_string1)
            string = string.replace(ope_token.group(0), ' ', 1)
            string = string.lstrip()
        # seperator
        elif(sep_token != None):
            new_string2 = "<sep, " + sep_token.group(0) + ">"
            result.append(new_string2)
            string = string.replace(sep_token.group(0), ' ', 1)
            string = string.lstrip()
        # identifier
        elif(id_token != None):
            new_string3 = "<id, " + id_token.group(0) + ">"
            result.append(new_string3)
            string = string.replace(id_token.group(0), '', 1)
            string = string.lstrip()
        # integer lit
        elif(int_token != None):
            new_string4 = "<lit, " + int_token.group(0) + ">"
            result.append(new_string4)
            string = string.replace(int_token.group(0), '', 1)
            string = string.lstrip()
        # float lit
        elif(float_token != None):
            new_string5 = "<lit, " + float_token.group(0) + ">"
            result.append(new_string5)
            string = string.replace(float_token.group(0), '', 1)
            string = string.lstrip()
        # string lit
        elif(string_token != None):
            new_string6 = "<lit, " + string_token.group(0) + ">"
            result.append(new_string6)
            string = string.replace(string_token.group(0), '', 1)
            string = string.lstrip()
        else:
            print("Cannot process the below input:")
            print(string)
            string = ""
    print(result)


if __name__ == "__main__":
    print("input: int    A1=5")
    cutonelinetokens("int    A1=5")
    print("float BBB2     =1034.2")
    cutonelinetokens("float BBB2     =1034.2")
    print("float     cresult     =     A1     +BBB2     *      BBB2")
    cutonelinetokens(
        "float     cresult     =     A1     +BBB2     *      BBB2")
    print("if     (cresult     >10):")
    cutonelinetokens("if     (cresult     >10):")
    print('print("TinyPie    "    )')
    cutonelinetokens('print("TinyPie    "    )')
