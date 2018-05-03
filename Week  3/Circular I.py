"""Circular I"""
def main():
    """It will show yong"""
    x_me = float(input())
    y_me = float(input())
    cir = float(input())
    x_yong = float(input())
    y_yong = float(input())
    eiei = ((x_yong - x_me)**2 + (y_yong - y_me)**2)**(0.5)
    if eiei <= cir:
        print("Yes")
    else:
        print("No")
main()
