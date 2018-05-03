"""Circular II"""
def main():
    """It will show yong"""
    x_me = float(input())
    y_me = float(input())
    cir = float(input())
    x_fri = float(input())
    y_fri = float(input())
    cir_2 = float(input())
    eiei = ((x_fri - x_me)**2 + (y_fri - y_me)**2)**(0.5)
    if eiei < cir + cir_2:
        print("Yes")
    else:
        print("No")
main()
