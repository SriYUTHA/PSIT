"""PickThemAgain"""
def main():
    """Doc"""
    num = input().split()
    num = [int(x) for x in num]
    results = []
    for i in num:
        if i%3 == 0 or i%5 == 0:
            results.append(i)
    if len(results) == 0:
        print("Nope")
    else:
        for i in reversed(results):
            print(i)
main()
