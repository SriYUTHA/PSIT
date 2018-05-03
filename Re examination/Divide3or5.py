"""Divide3or5"""
def main():
    """Count plus num"""
    num = float(input())
    ans = 0
    for i in range(1, int(num+1)):
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    print(ans)
main()
