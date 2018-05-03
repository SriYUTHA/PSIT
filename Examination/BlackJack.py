"""BlackJack"""
def main():
    """BlackJack"""
    num = int(input())
    score = 0
    ace = 0
    for _ in range(num):
        card1 = input()
        if card1 in "JQK":
            score += 10
        elif card1 == "A":
            score += 11
            ace += 1
        else:
            score += int(card1)
    while 1:
        if score <= 21 or ace == 0:
            break
        score -= 10
        ace -= 1
    print(score)
main()
