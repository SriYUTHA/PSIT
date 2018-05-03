"""Day2011"""
def main():
    """day in 2011"""
    date = int(input())
    mount = int(input())
    allday = 0
    list_day = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    list_m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in list_m[0:mount-1]:
        allday += i
        if mount == 1:
            allday = 0
    allday += date
    ans = (allday%7)-1
    print(list_day[ans])
main()
