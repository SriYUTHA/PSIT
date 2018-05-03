"""HelloWorldComeBack"""
def language():
    """This code print Thai or English"""
    eng = 'abcdefghijklmnopqrstuvwxyz'
    txt = input()
    if  txt[0].lower() in eng:
        print("Hello", txt + ".")
    else:
        print("สวัสดี", txt)
language()
