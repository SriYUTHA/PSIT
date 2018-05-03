"""Stepper II"""
def main():
    """number plus"""
    start = int(input())
    stop = int(input())
    if start < stop:
        for i in range(start, stop+1):
            print(i)
    elif start == stop:
        print(start)
    else:
        for i in range(start, stop-1, -1):
            print(i)
main()
