"""linesorting"""
def main(num):
    """sort"""
    show = []
    for i in range(num):
        txt = input()
        show.append(txt)
    ans = sorted(show, key=len)
    for i in ans:
        print(i)
main(int(input()))
