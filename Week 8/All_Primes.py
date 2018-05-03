"""All_Primes"""
def main():
    """it will you how many prime numbers"""
    numbers = int(input())
    count = 0
    for num in range(1, numbers+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                count += 1
    print(count)
main()
