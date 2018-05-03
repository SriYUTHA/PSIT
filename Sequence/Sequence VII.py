"""Sequence VII"""
def main():
    """This code prints the sequence of number"""
    num = int(input())
    for i in range(num, 0, -1):
        for k in range(1, num-(i-1)):
            if k == num-i:
                print(k, end="\n")
            elif k < num-i:
                print(k, end=" ")
    for i in range(0, num+1):
        for k in range(1, num-(i-1)):
            if k == num-i:
                print(k, end="\n")
            elif k < num-i:
                print(k, end=" ")
main()
