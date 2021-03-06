def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

#2. Try doing this: help(ex25) and also help(ex25.break_words). Notice how you get help for your module, and how the help is those odd """ strings you put after each function in ex25? Those special strings are called documentation comments and we'll be seeing more of them.
"""
help(ex25)
Help on module ex25:

NAME
    ex25

FILE
    /root/Desktop/LPTHW/ex25.py

FUNCTIONS
    break_words(stuff)
        This function will break up words for us.

    print_first_and_last(sentence)
        Prints the first and last words of the sentence.

    print_first_and_last_sorted(sentence)
        Sorts the words then prints the first and last one.

    print_first_word(words)
        Prints the first word after popping it off.

    print_last_word(words)
        Prints the last word after popping it off.

    sort_sentence(sentence)
        Takes in a full sentence and returns the sorted words.

    sort_words(words)
        Sorts the words.

help(ex25.break_words)
Help on function break_words in module ex25:

break_words(stuff)
    This function will break up words for us.
"""

#3. Typing ex25. is annoying. A shortcut is to do your import like this: from ex25 import * which is like saying, "Import everything from ex25." Programmers like saying things backward. Start a new session and see how all your functions are right there.
"""
root@kali:~/Desktop/LPTHW# python
Python 2.7.3 (default, Mar 14 2014, 11:57:14)
[GCC 4.7.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from ex25 import *
>>>
"""

"""
How can the words.pop function change the words variable?
That's a complicated question, but in this case words is a list, and because of that you can give it commands and it'll retain the results of those commands. This is similar to how files and many other things worked when you were working with them.

When should I print instead of return in a function?
The return from a function gives the line of code that called the function a result. You can think of a function as taking input through its arguments, and returning output through return. The print is completely unrelated to this, and only deals with printing output to the terminal.
"""
