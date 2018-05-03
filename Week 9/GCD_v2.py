"""GCD_v2"""
def main():
    """Find gcd"""
def gcd(num1, num2):
    """gcd"""
    if num1 > num2:
        number = num1 % num2
        if number == 0:
            return num2
        else:
            return gcd(num2, number)
    if num1 < num2:
        number = num2 % num1
        if number == 0:
            return num1
        else:
            return gcd(num1, number)
print(gcd(int(input()), int(input())))
main()
