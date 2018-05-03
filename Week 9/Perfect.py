"""Perfect"""
def main():
    """show sum perfect number of limit input"""
    limit = int(input())
    sieve = [1] * (limit + 1)
    show = []
    num = 2
    while num <= limit:
        if sieve[num] == num:
            show.append(num)
        knum = 2 * num
        while knum <= limit:
            sieve[knum] += num
            knum += num
        num += 1
    print(sum(show))
main()
