"""Median"""
def main():
    """ Find the median number """
    num = int(input())
    num_list = sorted([float(input()) for i in range(num)])
    if num % 2 != 0:
        print("%.1f"%float(num_list[num//2]))
    else:
        ans = float((num_list[num//2]+num_list[num//2-1])/2)
        print("%.1f"%ans)
main()
