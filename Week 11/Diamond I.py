"""Diamond I"""
def main(line, row, list_row, list_ans, count):
    """Find the maximum value of diamonds dug into the vertical ?"""
    list_set_num = list(input().split() for _ in range(line))
    for _ in range(row):
        for i in list_set_num:
            list_num = i
            list_row.append(int(list_num[count]))
        list_ans.append(sum(list_row))
        list_row = []
        count += 1
    print(max(list_ans))
main(int(input()), int(input()), [], [], 0)
