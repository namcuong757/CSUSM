from pickle import FALSE, TRUE
import re


def remove_token(str, token):
    i = 0
    while i < len(token):
        if token[i] != '':
            str = str.replace(token[i], " ")
        i += 1
    return str


def find_keyword(lis):
    temp = re.compile(r"(\bif\b)|(\belse\b)|(\bfloat\b)|(\bint\b)")
    token = temp.findall(lis)
    result = []
    for j in token:
        for i in j:
            if i != '':
                result.append(i)
    return result


def find_operator(lis):
    return re.findall(r"\+|\*|=|>", lis)


def find_seperator(lis):
    return re.findall(r"\(|\)|:|\"|;", lis)


def find_indentifier(lis):
    token = re.findall(r"([A-Za-z]+\d+)|([A-Za-z]+)", lis)
    result = []
    for j in token:
        for i in j:
            if i != '':
                result.append(i)
    return result


def find_int_literal(lis):
    return re.findall(r"(?<!\S)\d+(?!\S)", lis)


def find_float_literal(lis):
    return re.findall(r"\d+\.\d+", lis)


def find_string_literal(lis):
    token = re.compile(r'(["\'])((?:\\.|[^\\])*?)(\1)').findall(lis)
    result = []
    i = 0
    for j in token:
        for i in j:
            if i != '"':
                result.append(i)
    return result


if __name__ == "__main__":
    result = []
    print("Hit enter to terminate")
    while(TRUE):
        print("Enter code line: ")
        user_input = input()
        if user_input == "":
            exit()
        user_input = " ".join(user_input.split())
        print("user_input: " + user_input)
        keyw_token = find_keyword(user_input)
        user_input = remove_token(user_input, keyw_token)
        op_token = find_operator(user_input)
        user_input = remove_token(user_input, op_token)
        sepe_token = find_seperator(user_input)
        user_input = remove_token(user_input, sepe_token)
        iden_token = find_indentifier(user_input)
        user_input = remove_token(user_input, iden_token)
        int_lit_token = find_int_literal(user_input)
        user_input = remove_token(user_input, int_lit_token)
        float_lit_token = find_float_literal(user_input)
        user_input = remove_token(user_input, float_lit_token)
        string_lit_token = find_string_literal(user_input)
        if keyw_token:
            for i in keyw_token:
                keyword_pair = "<key," + i + ">"
                result.append(keyword_pair)
        if op_token:
            for i in op_token:
                op_pair = "<op," + i + ">"
                result.append(op_pair)
        if sepe_token:
            for i in sepe_token:
                sepe_pair = "<sep," + i + ">"
                result.append(sepe_pair)
        if iden_token:
            for i in iden_token:
                iden_pair = "<id," + i + ">"
                result.append(iden_pair)
        if int_lit_token:
            for i in int_lit_token:
                int_lit_pair = "lit," + i + ">"
                result.append(int_lit_pair)
        if float_lit_token:
            for i in float_lit_token:
                float_lit_pair = "lit," + i + ">"
                result.append(float_lit_pair)
        if string_lit_token:
            for i in string_lit_token:
                string_lit_pair = "lis," + i + ">"
                result.append(string_lit_pair)
        print(result)
        result.clear()
