"""RuleofThree"""
def main():
    """This code print product is worthwhile"""
    var = int(input())
    psize = 0
    pprice = -1
    for _  in range(var):
        price = float(input())
        size = float(input())
        ptemp = psize/pprice
        temp = size/price
        if temp > ptemp:
            ptemp = temp
            psize = size
            pprice = price
        elif temp == ptemp and pprice > price:
            psize = size
            pprice = price
    print("%.2f %.2f" %(pprice, psize))
main()
