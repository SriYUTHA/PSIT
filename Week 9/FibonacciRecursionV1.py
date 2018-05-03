"""FibonacciRecursionV1"""
def main():
    """It will show Fibonacci"""
    num = int(input())
    ans = fibo(num)
    print(ans)
def fibo(var):
    """fiboeiei"""
    if var == 0:
        return 0
    if var == 1:
        return 1
    if var == 2:
        return 1
    else:
        return fibo(var-1) + fibo(var-2)
main()
