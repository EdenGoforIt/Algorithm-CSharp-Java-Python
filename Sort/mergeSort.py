def merge_sort(a):
    n = len(a)

    # if there is only one, nothing to do
    if n <= 1:
        return a

    mid = n // 2

    g1 = merge_sort(a[:mid])  # recursive

    g2 = merge_sort(a[mid:])  # recursive

    result = []

    while g1 and g2:

        if g1[0] < g2[0]:     # compare the first value of each group
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    # add rest of them into the result, the order which group comes first doesn't matter
    while g1:

        result.append(g1.pop(0))

    while g2:

        result.append(g2.pop(0))
    return result


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

print(merge_sort(d))
