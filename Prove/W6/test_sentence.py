"""
File: test_sentence.py
Author: Luis Andrade
Date: 13 Febraury 2023
Purpose: Prove that you can write and troubleshoot a program that contains multiple functions..
"""
from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_sentence
import random
import pytest

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    single_nouns = ["bird", "boy", "car", "cat","child", "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):
        word = get_noun(1)
        assert word in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats","childrens", "dogs", "girls", "men", "rabbits", "women"]
    
    for _ in range(4):
        word = get_noun(2)
        assert word in plural_nouns
    

def test_get_verb():
    past_verb = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        word = get_verb(1,"past")
        assert word in past_verb

    present_single_verb = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        word = get_verb(1,"present")
        assert word in present_single_verb

    present_plural_verb = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        word = get_verb(2,"present")
        assert word in present_plural_verb

    future_verb = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(4):
        word = get_verb(1,"future")
        assert word in future_verb


def test_get_preposition():
    # Test the prepositions.

    prepositions = ['about', 'above', 'across', 'after', 'along',
        'around', 'at', 'before', 'behind', 'below',
        'beyond', 'by', 'despite', 'except', 'for',
        'from', 'in', 'into', 'near', 'of',
        'off', 'on', 'onto', 'out', 'over',
        'past', 'to', 'under', 'with', 'without']

# This loop will repeat the statements inside it 4 times.    
    for _ in range(4):

        # Call the get_preposition function which should return a preposition.
        word = get_preposition()

        # Verify that the verb returned from get_preposition
        # is one of the prepositions in the prepositions list.
        assert word in prepositions

def test_get_prepositional_phrase():    
    prepositions = ['about', 'above', 'across', 'after', 'along',
        'around', 'at', 'before', 'behind', 'below','beyond', 'by', 
        'despite', 'except', 'for', 'from', 'in', 'into', 'near', 'of',
        'off', 'on', 'onto', 'out', 'over', 'past', 'to', 'under', 
        'with', 'without']    
    single_determiners = ['a', 'one', 'the']
    plural_determiners = ['some', 'many', 'the']
    single_nouns = ['bird', 'boy', 'car', 'cat', 'child', 'dog',
        'girl', 'man', 'rabbit', 'woman']
    plural_nouns = ['birds', 'boys', 'cars', 'cats', 'children',
        'dogs', 'girls', 'men', 'rabbits', 'women']

    # Test the single prepositional phrase.
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_prepositional_phrase function which
        # should return a single prepositional phrase.
        single_prepositional_phrase = get_prepositional_phrase(1)
        # Call split function to save each word belonging to preposition_phrase 
        # in the words list. 
        words = single_prepositional_phrase.split(' ')
        preposition = words[0]
        determiner = words[1]
        noun = words[2]

        # Test the number of words contained in words list.
        assert len(words) == 3                        
        # Test the preposition is in presitions list.
        assert preposition in prepositions
        # Test the determiner is in single_determiners list.
        assert determiner in single_determiners
        # Test the noun is in single_nouns list.
        assert noun in single_nouns

    # 2. Test the plural prepositional phrase.
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_prepositional_phrase function which
        # should return a plural prepositional phrase.
        plural_prepositional_phrase = get_prepositional_phrase(2)
        words = plural_prepositional_phrase.split(' ')
        preposition = words[0]
        determiner = words[1]
        noun = words[2]
        
        # Test the number of words contained in words list.
        assert len(words) == 3        
        # Test the preposition is in presitions list.
        assert preposition in prepositions
        # Test the determiner is in plural_determiners list.
        assert determiner in plural_determiners
        # Test the noun is in plural_nouns list.
        assert noun in plural_nouns

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])