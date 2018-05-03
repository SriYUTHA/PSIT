""" inverter """
def main(num):
    """ inverter """
    print(int("".join(num)) if int("".join(num)) != 0 else "")
main(['0' if i == '1' else '1' for i in input()])
