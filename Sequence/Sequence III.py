"""Sequence III"""
def main():
    """count number 3"""
    num = int(input())
    for j in range(2, num+2):
        for i in range(j, num+j):
            print(i, end=' ')
        print(sep=' ')
main()
