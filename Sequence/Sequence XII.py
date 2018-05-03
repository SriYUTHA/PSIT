"""Sequence XII"""
def boot():
    """Square"""
    num = int(input())
    for i in range(num):
        for j in range(i, 0, -1):
            print("%02d"%(num-j), end=" ")
        for j in range(num, i, -1):
            print("%02d"%(j), end=" ")
        for j in range(i+2, num+1):
            print("%02d"%(j), end=" ")
        for j in range(num-1, num-i-1, -1):
            print("%02d"%(j), end=" ")
        print()
    for i in range(num-1):
        for j in range(i+2, num+1):
            print("%02d"%(j), end=" ")
        for j in range(num-1, num-i-2, -1):
            print("%02d"%(j), end=" ")
        for j in range(num-i, num):
            print("%02d"%(j), end=" ")
        for j in range(num, i+1, -1):
            print("%02d"%(j), end=" ")
        print()
boot()
