"""FOR!F-Ball"""
def main():
    """it will show ball"""
    list_text = list(input())
    point = ["ball", "glass", "glass"]
    count = 0
    for i in list_text:
        if i == "A":
            point[0], point[1] = point[1], point[0]
        elif i == "B":
            point[1], point[2] = point[2], point[1]
        elif i == "C":
            point[0], point[2] = point[2], point[0]
    for i in point:
        count += 1
        if i == "ball":
            print(count)
main()
