"""Donut"""
def main():
    """Donut"""
    cost = int(input())
    num_buy = int(input())
    num_free = int(input())
    num_want = int(input())
    pack = num_want//(num_buy+num_free)
    remain = num_want%(num_buy+num_free)
    get_donut = 0
    cost_all = 0
    if remain >= num_buy:
        pack += 1
    else:
        get_donut += remain
        cost_all += cost*remain
    cost_all += pack*num_buy*cost
    get_donut += pack*(num_free+num_buy)
    print(cost_all, get_donut)
main()
