"""SceneSwitch I"""
def  main():
    """Docstring"""
    count1 = 0
    count2 = 0
    count3 = 0
    num1 = 0
    num2 = 0
    while 1:
        count1 += 1
        num = input()
        if num == "End":
            break
        num2 = num1
        num1 = float(num)
        if count1 == 1 or count1 == 2:
            continue
        if count1 % 2 != 0 and count3 == 0:
            if num1 - num2 <= 6:
                count2 += 1
                count3 += 1
        elif count1 %2 == 0:
            continue
        else:
            count3 = 0
    print(count2)
main()
