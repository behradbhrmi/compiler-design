from string import punctuation as punc


PRONOUN = "ضمیر"
VERB = "فعل"
NOUN = "اسم"
ADJECTIVE = "صفت"
ADVERB = "قید"
PREPOSITION = "حرف اضافه"
INTEGER = "عدد"


my_dict = {
    "من":PRONOUN,
    "تو":PRONOUN,
    "او":PRONOUN,
    "ما":PRONOUN,
    "شما":PRONOUN,
    "خوب":ADJECTIVE,
    "عالی":ADJECTIVE,
    "بد":ADJECTIVE,
    "کتاب":NOUN,
    "خوند":VERB,
    "خرید":VERB,
    "خورد":VERB,
    "دید":VERB,
    "برد":VERB,
    "با":PREPOSITION,
    "به":PREPOSITION,
    "را":PREPOSITION
    
}

result = {}


def verb_checker(verb:str) -> bool:
    verbs_list = [item[0] for item in my_dict.items() if item[1] == VERB]

    if verb in verbs_list:                      return True
    elif  verb.replace('م', '') in verbs_list:  return True
    elif verb.replace('ی', '') in verbs_list:   return True
    elif verb.replace('یم', '') in verbs_list:  return True
    elif  verb.replace('ید', '') in verbs_list: return True
    else:                                       return False


def word_counter(word:str, word_type) -> None:
    try:
        if result[word.lower()]["count"]:
            result[word.lower()]["count"] += 1
    except:
        temp = {
            word.lower(): 
            {
                'count' : 1,
                'type' : word_type,},
        }
        result.update(temp)


def word_checker(word:str) -> None:
    try:
        try:
            int(word)
            return INTEGER
        except:
            return my_dict[word.lower()]
    except ValueError:
        print("ERROR : Invalid Word")
        

def spliter(sentence:str) -> list:
    return sentence.strip(punc).split()


def lexical_analyser(sentence:str) -> dict:
    seperated_words = spliter(sentence)
    for word in seperated_words:
        if verb_checker(word):
            word_counter(word, VERB)

        elif word_type:=word_checker(word):
            word_counter(word, word_type)
    return result


def result_printer(result:dict) -> None:
    print('Result:')
    for word, val in result.items():
        print(f"Word: {word.title()} \t Count: {val['count']} \t Type: {val['type']}")


def main():
    sentence = "من کتاب 2 را خوندم"
    lexical_analyser(sentence)
    result_printer(result)


if __name__ == '__main__':
    main()
