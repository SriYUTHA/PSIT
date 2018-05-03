"""BootSequence"""
def main():
    """Count number"""
    num = int(input())
    for i in range(num+1):
        for i in range(1, num):
            print(i, end=" ")
        print(num)
main()
