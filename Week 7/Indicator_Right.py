"""Indicator_Right"""
def main():
    """it will show *"""
    width = int(input())
    height = int(input())
    space = height//2
    for i in range(-space, space+1):
        print(" "*(space-abs(i))+"*"*width)
main()
