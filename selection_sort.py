def selection_sort(lst):
    ln = len(lst)
    for i in range(ln):
        mnindx = i
        for j in range(i + 1, ln):
            if lst[j] < lst[mnindx]:
                mnindx = j
        if mnindx != i:
            lst[i], lst[mnindx] = lst[mnindx], lst[i]
    return lst


print(selection_sort([98, 23, 45, 76, 12, 93, 11, 10, 4, 5, 9, 16]))
