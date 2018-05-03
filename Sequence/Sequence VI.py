"""Sequence VI"""
def main():
    """count number 6"""
    num = int(input())
    for i in range(1, num+1):
        for j in range(1, num-num+i):
            print(j, end=' ')
        print(i, sep='\n')
main()
