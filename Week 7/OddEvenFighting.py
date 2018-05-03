"""OddEvenFighting"""
def main():
    """it will show who win this"""
    team_even = 0
    team_odd = 0
    while 1:
        num = int(input())
        if num == 0:
            break
        if num%2 == 0:
            team_even += num
        if num%2 != 0:
            team_odd += num
    if team_even > team_odd:
        print("Even", team_even)
    if team_odd > team_even:
        print("Odd", team_odd)
    if team_odd == team_even:
        print("Draw", team_odd)
main()
