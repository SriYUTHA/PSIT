"""Sequence I"""
def main():
    """Count number 1"""
    num = int(input())
    for i in range(num):
        for i in range(1, num):
            print(i, end=" ")
        print(num)
main()
