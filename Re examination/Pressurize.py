"""Pressurize"""
def pressure():
    """Find Underpressure & Overpressure & Safe """
    press_in = float(input())
    press_out = float(input())
    dif = (abs(press_in-press_out)/press_in)*100
    if dif <= 30:
        print("Safe %.4f" %dif + "%", end="")
    if press_out < press_in and dif > 30:
        print("Underpressure %.4f" %dif + "%", end="")
    elif press_out > press_in and dif > 30:
        print("Overpressure %.4f" %dif + "%", end="")
pressure()
