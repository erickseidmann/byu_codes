from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

   
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():

    single_nouns = [ "bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):
        nouns = get_noun(1)
        assert nouns in single_nouns
    
    plural_nouns = [ "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):
        nouns = get_noun(2)
        assert nouns in plural_nouns

def test_get_verb():

    single_verb = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):
        verb = get_verb(1,"present")
        assert verb in single_verb
    
    plural_verb = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]

    for _ in range(4):
        verb = get_verb(2,"present")
        assert verb in plural_verb
    
    future_verb = [ "will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]

    for _ in range(4):
        verb = get_verb(2,"future")
        assert verb in future_verb

def test_get_preposition():

    prepositions = [ "about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(4):
        preposition = get_preposition()
        assert preposition in prepositions

def test_get_prepositional_phrase():
    
    prepositional_pharese_complet = get_preposition()+ get_determiner(1)+ get_noun(1)

    for _ in range(4):
        prepositional_pharese = get_prepositional_phrase(1)
        prepositional_pharese_complet = prepositional_pharese.split()
        assert prepositional_pharese in prepositional_pharese_complet


pytest.main(["-v","--tb=line","-rN",__file__])