"""WordSequence II"""
def main():
    """It will sum 2 text"""
    text1 = input()
    text2 = input()
    count = 1
    if len(text1) >= len(text2):
        num = len(text1)
    else:
        num = len(text2)
    for i in range(num+1):
        if i == 0:
            print(text1)
        else:
            print(text2[:count] + text1[count:])
            count += 1
main()
