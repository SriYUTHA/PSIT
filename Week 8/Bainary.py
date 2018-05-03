"""Binary"""
def  main():
    """It will show binary"""
    num = int(input())
    l_1 = []
    if num >= 1:
        while 1:
            if num == 1:
                l_1.append(1)
                break
            if num%2 == 0:
                num = num//2
                l_1.append(0)
                continue
            if num%2 != 0:
                num = num//2
                l_1.append(1)
    for i in reversed(l_1):
        print(i, end="")
    if num == 0:
        print("0")
main()
