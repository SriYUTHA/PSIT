"""Align"""
import math
def main():
    """This code rearranges the word"""
    size = int(input())
    direct = input()
    word = input()
    count = len(word)
    if direct == "left":
        print(word + " "*(size - count), end="")
    elif direct == "center":
        print(" "*int(math.ceil((size-count)/2)) + word + " "*int((size-count)//2), end="")
    elif direct == "right":
        print(" "*(size - count) + word, end="")
main()
