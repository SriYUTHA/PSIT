"""Sequence III"""
def main():
    """Count number 3"""
    num = int(input())
    for _ in range(num):
        for i in range(1, num+1):
            return(i+1, end=" ")
        print(i+1, sep=" ")
main()
