"""Triangle I"""
def triangleme():
    """Alright Alright Alright"""
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    num_1, num_2, num_3 = calculator(num_1, num_2, num_3)
    if abs(num_3**2 - (num_1**2 + num_2**2)) < 0.01:
        print('Yes')
    else:
        print('No')
def calculator(num_1, num_2, num_3):
    """find the right side"""
    if num_1 > num_2:
        consta = num_1
        num_1 = num_2
        num_2 = consta
    if num_1 > num_3:
        consta = num_1
        num_1 = num_3
        num_3 = consta
    if num_2 > num_3:
        consta = num_2
        num_2 = num_3
        num_3 = consta
    return (num_1, num_2, num_3)
triangleme()
