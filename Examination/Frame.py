"""Frame"""
def main():
    """picture in frame"""
    txt = str(input())
    print('*' * (len(txt)+2))
    print('*' + txt + '*')
    print('*' * (len(txt)+2))
main()
