"""Sequence IV"""
def main():
    """count number 4"""
    num = int(input())
    for j in range(num):
        for i in range(1, num+1):
            print(i+num*j, end=' ')
        print(sep=' ')
main()
