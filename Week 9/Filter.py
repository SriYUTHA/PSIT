"""Filter"""
import json
def main():
    """Filter"""
    txt = input()
    txt = json.loads(txt)
    num = float(input())
    list_1 = []
    for i in txt:
        if txt[i] >= num:
            list_1.append(i)
    list_1.sort()
    if list_1 == []:
        print("Nope")
    else:
        for i in list_1:
            print("%s\t%.2f"%(i, txt[i]))
main()
