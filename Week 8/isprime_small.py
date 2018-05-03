"""isprime_small"""
def main():
    """it will check prime number or not"""
    numbers = int(input())
    count = 0 #count how many numbers can / or not
    if numbers > 1:
        for i in range(2, numbers):
            if numbers%i == 0:
                count += 1
        if count == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
main()
