"""SqFree"""
def sqfree(num):
    """checker"""
    for i in range(2, int(num**0.5)+1):
        if num%(i**2) == 0:
            return 0
    return 1
def count_sqfree(num):
    """show ans"""
    count = 0
    for i in range(1, num+1):
        if sqfree(i):
            count = count + 1
    return count
print(count_sqfree(int(input())))
