"""Sequence VIII"""
def main():
    """count number"""
    num = int(input())
    for i in range(num):
        print(' '*3*(num-i-1), end='')
        for j in range(1, i+2):
            print('%02d ' % j, end='')
        print()
main()
