"""Turnstile"""
def main():
    """Count people pessed door"""
    state = 'locked'
    count = 0
    while True:
        action = input()
        if action == 'END':
            break
        if state == 'locked' and action == 'C':
            state = 'unlocked'
            continue
        if state == 'locked' and action == 'P':
            continue
        if state == 'unlocked' and action == 'C':
            continue
        if state == 'unlocked' and action == 'P':
            count += 1
            state = 'locked'
    print(count)
main()
