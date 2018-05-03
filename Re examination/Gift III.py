"""Gift III"""
def main():
    """Gift to boss"""
    box1 = 0
    box2 = 0
    amount = int(input())
    for _ in range(amount):
        num1 = int(input())
        if num1 > box1:
            box2 = box1
            box1 = num1
        elif num1 > box2 and num1 < box1:
            box2 = num1
    if box2 == 0:
        print("Exit")
    elif box1 > box2:
        print("%d" %box2)
main()
