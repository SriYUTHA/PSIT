"""Classify"""
def main():
    """Grade Year to show the highest year (old)"""
    idall = []
    id_lite = []
    year = 0
    while 1:
        num = input()
        if num == "END":
            break
        idall.append(num)
        if num[:4] not in id_lite:
            id_lite.append(num[:4])
    id_lite.sort()
    for i in id_lite:
        count = 0
        for j in idall:
            if i == j[:4]:
                count += 1
        if i[:2] == year:
            print("-- %s %d"%(int(i[2:4]), count))
        else:
            print("%2s %s %d"%(i[:2], int(i[2:4]), count))
        year = i[:2]
main()
