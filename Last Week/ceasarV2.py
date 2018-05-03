""" ceasar """
def decrypt(key, text):
    """ input and decrypt with key """
    char_lower = "abcdefghijklmnopqrstuvwxyz"
    char_upper = char_lower.upper()
    ans = ""
    for i in text:
        if i.islower():
            ans += char_lower[(char_lower.find(i)+key)%26]
        elif i.isupper():
            ans += char_upper[(char_upper.find(i)+key)%26]
        else:
            ans += i
    return ans
def main():
    """ main function """
    text = input()
    possible = ['is', 'are', 'what', 'why', 'where', 'when', 'how', 'am', "who", "also", \
    "was", "were", 'has', 'have', 'go', 'you', 'it', "they", 'the', 'said', "for", "in", \
    "and", "or", "with"]
    key = 0
    ans = ""
    while True:
        ans = decrypt(key, text)
        ans_de = ans.split()
        for item in possible:
            if item.lower() in ans_de:
                return ans
        key += 1
print(main())
