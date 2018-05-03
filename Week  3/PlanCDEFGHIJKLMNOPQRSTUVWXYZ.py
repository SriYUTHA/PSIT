"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main():
    """It will count number"""
    char = input()
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    if char == "Descend":
        chk_func1(num_1, num_2, num_3)
    elif char == "Ascend":
        chk_func2(num_1, num_2, num_3)
def chk_func1(num_1, num_2, num_3):
    """Docstring"""
    if num_1 >= num_2 >= num_3:
        print("%.2f, %.2f, %.2f"% (num_1, num_2, num_3))
    elif num_1 >= num_3 >= num_2:
        print("%.2f, %.2f, %.2f"% (num_1, num_3, num_2))
    elif num_2 >= num_1 >= num_3:
        print("%.2f, %.2f, %.2f"% (num_2, num_1, num_3))
    elif num_2 >= num_3 >= num_1:
        print("%.2f, %.2f, %.2f"% (num_2, num_3, num_1))
    elif num_3 >= num_2 >= num_1:
        print("%.2f, %.2f, %.2f"% (num_3, num_2, num_1))
    elif num_3 >= num_1 >= num_2:
        print("%.2f, %.2f, %.2f"% (num_3, num_1, num_2))
def chk_func2(num_1, num_2, num_3):
    """Docstring"""
    if num_1 <= num_2 <= num_3:
        print("%.2f, %.2f, %.2f"% (num_1, num_2, num_3))
    elif num_1 <= num_3 <= num_2:
        print("%.2f, %.2f, %.2f"% (num_1, num_3, num_2))
    elif num_2 <= num_1 <= num_3:
        print("%.2f, %.2f, %.2f"% (num_2, num_1, num_3))
    elif num_2 <= num_3 <= num_1:
        print("%.2f, %.2f, %.2f"% (num_2, num_3, num_1))
    elif num_3 <= num_2 <= num_1:
        print("%.2f, %.2f, %.2f"% (num_3, num_2, num_1))
    elif num_3 <= num_1 <= num_2:
        print("%.2f, %.2f, %.2f"% (num_3, num_1, num_2))
main()
