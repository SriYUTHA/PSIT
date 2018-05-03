"""Duplicate I"""
def main(people, people2):
    """DUPLICATE"""
    grop1 = []
    grop2 = []
    same = []
    for i in range(people):
        student = input()
        grop1.append(student)
    for i in range(people2):
        student = input()
        grop2.append(student)
    for i in min(grop1, grop2):
        if i in max(grop1, grop2):
            same.append(i)
    same.sort()
    if same == []:
        print("Nope")
    else:
        for i in same[::-1]:
            print(i)
main(int(input()), int(input()))
