"""LetterFrequency"""
def main():
    """ Get the most used character """
    word = input().lower()
    letterdict = {}
    for letter in word:
        if letter not in letterdict and letter.isalpha():
            letterdict[letter] = 1
        elif letter in letterdict and letter.isalpha():
            letterdict[letter] += 1
    print(max(letterdict, key=letterdict.get))
main()
