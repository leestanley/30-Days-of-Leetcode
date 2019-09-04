def two_unique(num):
    arr = []
    for i in range(len(num)):
        temp = num[i]
        num.pop(i)
        if temp not in num:
            arr.append(temp)
        num.append(temp)
    return arr


print(two_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))
