"""RemoveTag"""
def main():
    """it will show remove on string"""
    text1 = input()
    count_index = -1
    count_text = 0
    t_list = []
    num = 0
    count_spacial = 0
    empty_text = ""
    for i in text1:
        count_index += 1
        if i == "<" and count_text != 0:
            t_list.append(text1[num+1:num+count_text+1])
            count_text = 0
            count_spacial += 1
        elif i == ">":
            count_text = 0
            num = count_index
            count_spacial += 1
        else:
            count_text += 1
    if t_list == [] and count_spacial == 0:
        print(text1.split())
    else:
        for i in t_list:
            empty_text += i + " "
        aaa = empty_text.split()
        print(aaa)
main()
