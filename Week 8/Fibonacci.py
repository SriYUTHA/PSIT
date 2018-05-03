"""Fibonacci"""
def main():
    """i will show answer"""
    num = int(input())
    box2 = 0
    box1 = 1
    box3 = 0
    if num == 1:
        print("1")
    else:
        for i in range(1, num+1):
            if i == 1:
                continue
            box3 = box1 + box2
            box2 = box1
            box1 = box3
        print(box3)
main()
