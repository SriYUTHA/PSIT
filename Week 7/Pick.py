"""Pick"""
def pick():
    """FindDict"""
    import json
    dick = json.loads(input())
    key = input()
    if key in dick:
        print('Yes')
        print(dick[key])
    else:
        print('No')
pick()
