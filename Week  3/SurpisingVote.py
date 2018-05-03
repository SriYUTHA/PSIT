"""SurpisingVote"""
def main():
    """It will show surpise or not"""
    score_all = float(input())
    highest = float(input())
    score_2kon = score_all - highest
    lowest = score_2kon - highest
    if lowest < 0:
        lowest = 0
    if highest - lowest > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
