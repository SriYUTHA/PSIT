"""AlmostMean"""
def main(num):
    """Which student scores are almost out of the average?"""
    dictx = {}
    max_n = 0
    count = 0
    for i in range(num):
        txt = input().split("\t")
        dictx[txt[0]] = txt[1]
    for i in dictx:
        count += float(dictx[i])
    mean = count/num
    for i in dictx:
        if float(dictx[i]) < mean:
            if float(dictx[i]) > max_n:
                max_n = float(dictx[i])
                key = i
            else:
                max_n = max_n
                key = key
    print("%s\t%s" %(key, max_n))
main(int(input()))
