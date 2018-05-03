"""Sequence V"""
def main():
    """This code prints the sequence of number"""
    num = int(input())
    for i in range(num, 0, -1):
        if (i-1)%7 == num%7:
            print("%d" %(i), end="\n")
        else:
            print("%d" %(i), end=" ")
main()
