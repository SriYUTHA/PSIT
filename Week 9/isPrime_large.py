"""isPrime_large"""
def main():
    """it will check prime number or not"""
    numbers = int(input())
    count = 0 #count how many numbers can / or not
    if numbers > 1:
        for i in range(2, int(numbers**0.5)+1):
            if numbers%i == 0:
                count += 1
        if count == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
main()
