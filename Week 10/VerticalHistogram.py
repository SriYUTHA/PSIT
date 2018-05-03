"""vertical histogram"""
def main(text, list_1, list_2):
    """VerticalHistogram"""
    letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in letter:
        list_1.append(text.count(i))
        if i in text:
            list_2.append(i)
    for i in range(max(list_1), 0, -1):
        print('%03d' %i, end=' ')
        for j in list_2:
            if text.count(j) >= i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('   ', *list_2)
main(input(), [], [])
