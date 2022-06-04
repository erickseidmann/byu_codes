from ast import Return
import random
quantity= 1
tense ="futere"
def main ():
    get_determiner(quantity)
    get_noun(quantity)
    get_verb(quantity, tense)
    get_preposition()
    get_prepositional_phrase(quantity)
    

def get_determiner(quantity):
    """    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

   
    word = random.choice(words)
    return word 
def get_noun(quantity):
    """Return a randomly chosen noun.
        Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
      """
    if quantity == 1:
        nouns = [ "bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    nouns = random.choice(nouns)
    return nouns

def get_verb(quantity, tense):
    """Return a randomly chosen verb.

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if quantity == 1 and tense == "present":
        verb = [ "drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    elif quantity != 1 and tense == "present":
        verb = [ "drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    elif  quantity == 1 or quantity != 1  and tense == "future":
        verb = [ "will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    elif  quantity == 1 or quantity != 1  and tense == "past":
        verb = [ "drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    
    verb = random.choice(verb)
    return verb

def get_preposition():
    '''Return a randomly chosen preposition
    Return: a randomly chosen preposition.'''
    preposition =["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    preposition = random.choice(preposition)
    return preposition

def get_prepositional_phrase(quantity):
    prepositional_pharese = get_preposition()+ get_determiner(quantity)+ get_noun(quantity)

    return prepositional_pharese

  
main()
