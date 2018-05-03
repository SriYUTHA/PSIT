"""GCD_v1"""
def main():
    """find GCD"""
    num1, num2 = int(input()), int(input())
    while num2 != 0:
        num1, num2 = num2, num1%num2
    print(num1)
main()

