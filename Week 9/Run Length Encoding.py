"""Run Length Encoding"""
def run():
    """CountWordAndEncode"""
    keep = 1
    text = input()
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            keep += 1
        else:
            print(str(keep)+text[i-1], end="")
            keep = 1
        if i == len(text)-1:
            print(str(keep)+text[i])
run()
