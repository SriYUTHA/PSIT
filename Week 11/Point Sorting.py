"""Point Sorting"""
def pointsorting(num):
    """Point Sorting"""
    for _ in range(num):
        number = int(input())
        cal = [input().split() for _ in range(number)]
        cal = [(int(num1), int(num2)) for num1, num2 in cal]
        cal.sort(key=lambda x: (x[0] + x[1], x[0]))
        for num1, num2 in cal:
            print(num1, num2)
pointsorting(int(input()))
