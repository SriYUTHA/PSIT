"""Refrigerator"""
def main(_, foods):
    """calculate"""
    foods.sort()
    days = 0
    while foods[0] != 0:
        for i in range(1, len(foods)):
            foods[i] = foods[i] - 1
        days = days + 1
        foods.sort()
    return days
print(main(int(input()), [int(x) for x in input().split()]))
