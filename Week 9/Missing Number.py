"""Missing Number"""
def main():
    """Which numbers are missing?"""
    num_n = int(input())
    num_v = 0
    list_n = []
    list_i = []
    list_s = []
    for i in range(num_n+1):
        list_n.append(i)
    for _ in range(num_n):
        num_v = int(input())
        list_i.append(num_v)
        if num_v == 0:
            break
    for j in list_n:
        if j not in list_i:
            list_s.append(j)
            list_s.sort()
    for k in list_s:
        print(k)
main()
