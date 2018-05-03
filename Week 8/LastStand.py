"""LastStand"""
import json
def last():
    """print last number"""
    lis = json.loads(input())
    for i in lis:
        print(str(i)[-1])
last()
