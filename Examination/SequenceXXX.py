"""SequenceXXX"""
def main():
    """Doc"""
    size = int(input())
    number = int(input())
    for i in range(size):
        for _ in range(number):
            for j in range(size):
                condition = (i == 0)
                condition += (i == (size - 1))
                condition += (j == 0)
                condition += (j == (size - 1))
                condition += (i == j)
                condition += (j == (size - i - 1))
                if condition:
                    print("*", end="")
                else:
                    print(end=" ")
            print(end=" ")
        print()
main()
