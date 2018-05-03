"""Ascending"""
def ascend():
    """Sort numbers from ascending"""
    lis = []
    for i in range(5):
        num = int(input())
        lis.append(num)
    lis.sort()
    for i in lis:
        print(i)
ascend()
