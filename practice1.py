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

    case1 = True if verb in verbs_list else False
    case2 = True if verb.replace('ند', '') in verbs_list else False
    case3 = True if verb.replace('م', '') in verbs_list else False
    case4 = True if verb.replace('ی', '') in verbs_list else False
    case5 = True if verb.replace('ید', '') in verbs_list else False
    case6 = True if verb.replace('یم', '') in verbs_list else False

    result = case1 or case2 or case3 or case4 or case5 or case6
    
    return result

 

def word_counter(word:str, word_type) -> None:
    word = word.lower()

    try:
        result[word]["count"] += 1
    except:
        temp = {
            word:{
                'count' : 1,
                'type' : word_type,
                }
        }
        result.update(temp)


def word_checker(word:str) -> None:
    try:
        int(word)
        return INTEGER
    except:pass

    try:
        return my_dict[word.lower()]
        
    except ValueError:
        print("ERROR : Invalid Word")
        

def spliter(sentence:str) -> list:
    return sentence.strip(punc).split()


def analyser(sentence:str) -> dict:
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
    sentence = "من  من کتاب 2 را خوندم"
    analyser(sentence)
    result_printer(result)


if __name__ == '__main__':
    main()
