"""Password"""
import hashlib
def main():
    """Use hashing library"""
    text = input()
    hashing = hashlib.sha512(text.encode()).hexdigest()
    print(hashing.upper())
main()
