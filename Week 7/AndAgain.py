"""AndAgain"""
import json
def main():
    """Doc"""
    num1 = json.loads(input())
    num2 = json.loads(input())
    results = []
    for i in range(len(num1)):
        if num1[i]%2 != 0 and num2[i]%2 == 0:
            results.append(num1[i]+num2[i])
    if len(results) == 0:
        print("Nope")
    else:
        print(results)
main()
