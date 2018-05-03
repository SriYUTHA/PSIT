"""Day I"""
def main():
    """Find to year"""
    year = int(input())
    if year % 4 != 0:
        print("No")
    elif year % 4 == 0:
        if year % 100 == 0:
            if year % 400 != 0:
                print("No")
    if year % 4 == 0 and year % 100 != 0:
        print("Yes")
    elif year % 4 == 0 and year % 400 == 0:
        print("Yes")
main()
