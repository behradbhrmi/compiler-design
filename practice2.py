#  Letters variable shoud not start with
FORBBIDEN = '0123456789.@$%&*'

KEY_WORDS = ['if', 'else', 'and', 'not', 'int', 'input', 'print' '+', '=', '==', ';', ':', 'in']


def spliter(sentence:str) -> list:
    return sentence.split()

def check_if_valid_name(word:str) -> bool:
    return False if word[0] in FORBBIDEN else True

def check_if_key_word(word:str) -> bool:
    return True if word in KEY_WORDS else False

def check_if_integer(word:str) -> bool:
    try:
        int(word) 
        return True
    except:
        return False

def check_if_float(word:str) -> bool:
    try:
        float(word) 
        return True
    except:
        return False

def analyser(sentence:str) -> None:
    words = spliter(sentence)

    for word in words:

        result = check_if_key_word(word) or check_if_float(word) or check_if_integer(word) or check_if_valid_name(word)

        if not result:
            print("\033[91m {}\033[00m" .format(f">> Syntax Error :  '{word}' is not valid."))
            return

def main():
    sentence = "if x in @list"
    analyser(sentence)

if __name__ == '__main__':
    main()
