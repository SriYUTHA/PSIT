"""
    Program: BreachTheDoor
    Author: Sakorn & Warit
    Date: 15 Oct 2017
"""

import string

def main():
    """ Print out the word with 7 chars or greater """
    sentence = input()
    word_list = sentence.split(" ")
    numbers = "1234567890"

    for word in word_list:
        word = word.strip(string.punctuation + numbers)
        if len(word) > 6:
            print(word, end=" ")

main()
