import random
newlist = [random.randrange(-100, 100) for x in range(50)]
print(newlist)
for x in range(50):
    if newlist[x] > 0:
        print("положительное:", newlist[x])
    elif newlist[x] == 0:
        print("ноль это тоже число:", newlist[x], 'index: ', x)
    else:
        print("отрицательное:", newlist[x])