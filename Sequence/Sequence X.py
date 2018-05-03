"""Sequence X"""
def main():
    """This code prints the sequence of number"""
    num = int(input())
    for i in range(num-1, -1, -1):
        print(" "*(3*(i)), end="")
        for j in range(1, num-(i-1)):
            print("%.2d" %(j), end=" ")
        for k in range(num-i-1, 0, -1):
            print("%.2d" %(k), end=" ")
        print()
    for i in range(1, num):
        print(" "*(3*(i)), end="")
        for j in range(1, num-(i-1)):
            print("%.2d" %(j), end=" ")
        for k in range(num-i-1, 0, -1):
            print("%.2d" %(k), end=" ")
        print()
main()
