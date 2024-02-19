def bubble_sort(lst1):
    ln = len(lst1)
    i = 0
    srtd = False
    while not srtd:
        srtd = True
        for j in range(ln - i - 1):
            srtd = False
            if lst1[j] > lst1[j + 1]:
                lst1[j], lst1[j + 1] = lst1[j + 1], lst1[j]
        i += 1
    return lst1


print(bubble_sort([98, 23, 45, 76, 12, 93, 11, 10, 4, 5, 9, 16]))
