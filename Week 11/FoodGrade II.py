"""FoodGrade II"""
def main():
    """Eat food chicken"""
    count = 0
    cal = 0
    cal2 = []
    num = int(input())
    chk_1 = input().split()
    chk = [int(chicken) for chicken in chk_1]
    for i in sorted(chk):
        if cal < num:
            count += 1
            cal += int(i)
            cal2.append(int(i))
    if cal > num:
        cal -= max(cal2)
        count -= 1
    print(count)
main()
