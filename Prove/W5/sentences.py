import random

def main():
    grammatical_number = input("singular? (1) or plural?(2) ")
    tense = input("past, present, or future? ")
    quan = int(input("Prep phrase qauntity singular? (1) or plural?(2) "))
    det = get_determiner(grammatical_number)
    noun = get_noun(grammatical_number)
    verb = get_verb(grammatical_number,tense)
    prep_phrase = (get_prepositional_phrase(quan))
    print(str(det)+" "+str(noun)+" "+str(verb)+" "+str(prep_phrase)+".")

def get_preposition():
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    prep = get_preposition()
    det = get_determiner(quantity)
    noun = get_noun(quantity)
    prep_phrase = (str(prep)+" "+str(det)+" "+ str(noun))
    return prep_phrase

def get_determiner(grammatical_number):
    if grammatical_number == 1:
        words = ["the","one"]
    else:
        words = ["some","many"]
    word = random.choice(words)
    return word
def get_noun(grammatical_number):
    if grammatical_number ==1:
        words = ["adult", "bird", "boy", "car", "cat","child", "dog", "girl", "man", "woman"]
    else:
        words = ["adults", "birds", "boys", "cars", "cats","children", "dogs", "girls", "men", "women"]
    word = random.choice(words)
    return word

def get_verb(grammatical_number,tense):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    elif tense =="present":
        if grammatical_number == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    else:
        words = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    word = random.choice(words)
    return word


main()