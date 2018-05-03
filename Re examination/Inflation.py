"""Inflation"""
def main():
    """Doc"""
    money = float(input())
    years = int(input())
    money = int(money*100)
    dok = 10381
    for _ in range(years):
        money = money * dok
        money = money // 10000
    money_eiei = money // 100
    money_all = money % 100
    print("%d.%02d" %(money_eiei, money_all))
main()
