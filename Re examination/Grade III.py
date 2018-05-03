"""Grade III"""
def main():
    """It will show your print"""
    num = int(input())
    count = 0
    for _ in range(num):
        num2 = float(input())
        if 95 <= num2 <= 100:
            count += 4
        elif 90 <= num2 < 95:
            count += 3.5
        elif 85 <= num2 < 90:
            count += 3
        elif 80 <= num2 < 85:
            count += 2.5
        elif 75 <= num2 < 80:
            count += 2
        elif 70 <= num2 < 75:
            count += 1.5
        elif 65 <= num2 < 70:
            count += 1
        elif 60 <= num2 < 65:
            count += 0.5
        elif 0 <= num2 < 60:
            count += 0
    grade = count/num
    grade = int(grade*100)
    grade = grade/100
    print('%.2f' %grade)
main()
