"""Andagain6time"""
def main():
    """Andagain6time"""
    var = input()
    ttt = var.split()
    lll = []
    for i in ttt:
        herher = 0
        herher += i.count("a")
        herher += i.count("e")
        herher += i.count("i")
        herher += i.count("o")
        herher += i.count("u")
        if herher > 1:
            lll.append(i.strip("."))
    if lll == []:
        print("Nope")
    lll.sort()
    for eiei in lll:
        print(eiei)
main()
