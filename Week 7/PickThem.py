"""PickThem"""
import json
def main():
    """Doc"""
    num = input()
    results = []
    num = json.loads(num)
    for i in num:
        if i%2 == 0:
            results.append(i)
    if len(results) == 0:
        print("Nope")
    else:
        for i in results:
            print(i)
main()
