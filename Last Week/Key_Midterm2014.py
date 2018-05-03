"""Key_Midterm2014"""
def main():
    """find key"""
    txt = input()
    sum_num = 0
    for item in txt:
        sum_num += int(item)
    sum_num2 = int(txt[-3:])*10
    ans = sum_num+sum_num2
    if ans > 9999:
        print("%04d"%(ans%10000))
    elif ans < 1000:
        print("%04d"%(ans+1000))
    else:
        print("%04d"%(ans))
main()
