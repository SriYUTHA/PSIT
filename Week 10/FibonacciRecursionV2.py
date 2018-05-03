"""FibonacciRecursion V2 """
def fibo_memo(num, known):
    """show ans"""
    if num in known:
        return known[num]
    if num > 500:
        fibo_memo(num-500, known)
    res = fibo_memo(num-2, known) + fibo_memo(num-1, known)
    known[num] = res
    return res
print(fibo_memo(int(input()), {0:0, 1:1}))
