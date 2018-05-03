"""HorizontalHistogram"""
def main(txt):
    """HorizontalHistogram"""
    dict_txt = {}
    for j in txt:
        if j not in dict_txt:
            dict_txt[j] = 1
        else:
            dict_txt[j] += 1 #if sum hai += 1
    for ans, _ in sorted(dict_txt.items()):
        if ans.islower():
            print(ans, ':', end=' ')
            for i in range(dict_txt[ans]):
                if i%5 == 0 and i != 0:
                    print('|', end='')
                print('-', end='')
            print()
    for ans, _ in sorted(dict_txt.items()):
        if ans.isupper():
            print(ans, ':', end=' ')
            for i in range(dict_txt[ans]):
                if i%5 == 0 and i != 0:
                    print('|', end='')
                print('-', end='')
            print()
main(input())
