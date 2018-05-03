"""CoPrimeV1"""
def coprime():
    """Efficient check if two numbers are co-prime?"""
    num1 = int(input())
    num2 = int(input())
    ans = 0
    if num1 == 0 or num2 == 0:
        ans = num1+num2
    for i in range(min(num1, num2), 0, -1):
        if num1%i == 0 and num2%i == 0:
            ans += i
            break
    if ans > 1:
        print("NO", ans, sep='\n')
    else:
        print("YES", "1", sep='\n')
coprime()
