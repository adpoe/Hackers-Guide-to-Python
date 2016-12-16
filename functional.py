# example
# Non-pure function (modifies object in place)
def remove_last_item(mylist):
    """removes the last item from a list"""
    mylist.pop(-1) # this modifies the list

# A Pure function (!!!)
def butlast(mylist):
    """Like butlast in Lisp; returns the list without the last element"""
    return mylist[:-1] # this returns a copy of mylist

# Generators
# An object that returns a value on each call of its next() method
# until it raises StopIteration... implements the "iterator protocol" from PEP 255
# to CREATE a generator, just write a normal python function that contains a yield statement
# the fn returns when it gets to this point, then picks up here and returns value at next yield, next time it is called.
def mygenerator():
    yield 1
    yield 2
    yield 'a'

# can also check with a fn is a gnerator using this fn from inspect
inspect.isgeneratorfunction(mygenerator)
inspect.isgeneratorfunction(sum)

# in python 3, can also get the generator's current state
inspect.getgeneratorstate(gen)

# can also use the send() function, to call the generator like a function,
# the value in send() --> send(value) will be sent to the generator, and it'll
# return an appropriate response, given the info passed in. pretty cool. here's an example
def shorten(string_list):
    length = len(string_list[0])
    for s in string_list:
        length = yield s[:length]

mystringlist = [’loremipsum’, ’dolorsit’, ’ametfoobar’]
shortstringlist = shorten(mystringlist)
result = []
try:
    s = next(shortstringlist)
    result.append(s)
    while True:
        number_of_vowels = len(filter(lambda letter: letter in ’aeiou’, s))
        # Truncate the next string depending
        # on the number of vowels in the previous one
        s = shortstringlist.send(number_of_vowels)
        result.append(s)
except StopIteration:
    pass
# allows us to use generators like coroutines in Lua, & other languages

# tip:
# use one line generators, like list comprehensinos
gen = (x.upper() for x in [’hello’, ’world’])

# list comprehensions
# define a list's contents in line with its declaration
x = [i for i in (1,2,3)]
# yields => [1, 2, 3]

x = [word.capitalize()
     for line in (”hello world?”, ”world!”, ”or not”)
     for word in line.split()
     if not word.startswith(”or”)]
# yields => [’Hello’, ’World?’, ’World!’, ’Not’]

# tip:
# can also use set and dict comprehensions
>>> {x:x.upper() for x in [’hello’, ’world’]}
{’world’: ’WORLD’, ’hello’: ’HELLO’}
>>> {x.upper() for x in [’hello’, ’world’]}
set([’WORLD’, ’HELLO’])

# functional functions
# map (like clojure, haskell)
map(lambda x: x + ”bzz!”, [”I think”, ”I’m good”])
# yields => [’I thinkbzz!’, ”I’m goodbzz!”]

# list
# bread and butter of fn prog, map & filter =)
>>> list(filter(lambda x: x.startswith(”I ”), [”I think”, ”I’m good”]))
[’I think’]

# can also achieve same thing with list comprehensinos
[x + ”bzz!” for x in [”I think”, ”I’m good”]] # map
[x for x in [”I think”, ”I’m good”] if x.startswith(”I ”)] # filter

# enumerate
# use to create a sequence of numbered tuples
for i, item in enumerate(mylist):
    print(”Item %d: %s” % (i, item))
    
