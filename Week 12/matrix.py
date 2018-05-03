"""matrix"""
def main():
    """ Print matrix """
    row = int(input())
    col = int(input())
    matrix = [[float(input()) for _ in range(col)] for _ in range(row)]
    for row in matrix:
        for col in row:
            print("%d " %col, end='')
        print()
main()
