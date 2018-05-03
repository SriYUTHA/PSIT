"""Sequence XI"""
def boot():
    """Square"""
    num = int(input())
    for i in range(num):
        for j in range(i):
            print("%02d"%(j+1), end=" ")
        for j in range((num-i)*2-1):
            print("%02d"%(i+1), end=" ")
        for j in range(i, 0, -1):
            print("%02d"%(j), end=" ")
        print()
    for i in range(1, num):
        for j in range(num-i-1):
            print("%02d"%(j+1), end=" ")
        for j in range((i+1)*2-1):
            print("%02d"%(num-i), end=" ")
        for j in range((num-i)-1, 0, -1):
            print("%02d"%(j), end=" ")
        print()
boot()
