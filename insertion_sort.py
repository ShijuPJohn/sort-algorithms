def insertion_sort(lst):
    ln = len(lst)
    for i in range(1, ln):
        temp_val = lst[i]
        ipos = i - 1
        while lst[ipos] > temp_val and ipos >= 0:
            lst[ipos + 1] = lst[ipos]
            ipos -= 1
        lst[ipos + 1] = temp_val
    return lst


print(insertion_sort([98, 23, 45, 76, 12, 93, 11, 10, 4, 5, 9, 16]))
