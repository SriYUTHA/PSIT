"""BreakPassword"""
import hashlib
def main(text):
    """breakpass"""
    for i in range(100000):
        number = str("%05d" %i).encode('utf-8')
        if hashlib.sha512(number).hexdigest().upper() == text:
            print(str("%05d" %i))
            break
main(input())
