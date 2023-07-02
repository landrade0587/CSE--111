from sentences import get_determiner, get_noun, get_verb
import pytest

def test_get_determiner():
    single_determiners = ["a","the", "one"]
    for _ in range(4):
        word = get_determiner(1)
        assert word in single_determiners
    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)
        assert word in plural_determiners

def test_get_noun():
    single_noun = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    for _ in range(4):
        word = get_noun(1)
        assert word in single_noun
    plural_noun = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]
    for _ in range(4):
        word = get_noun(2)
        assert word in plural_noun

def test_get_verb():
    past_verb = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        word = get_verb(1,"past")
        assert word in past_verb
    present_single_verb = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        word = get_verb(1,"present")
        assert word in present_single_verb
    present_plural_verb = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        word = get_verb(2,"present")
        assert word in present_plural_verb
    future_verb = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in range(4):
        word = get_verb(1,"future")
        assert word in future_verb


pytest.main(["-v", "--tb=line", "-rN", __file__])