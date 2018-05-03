"""Run Length Decoding"""
def main(text):
    """Run Length Decoding"""
    num = ''
    for i in text:
        if i.isnumeric():
            num += i
        else:
            print(int(num)*i, end="")
            num = ''
main(input())

