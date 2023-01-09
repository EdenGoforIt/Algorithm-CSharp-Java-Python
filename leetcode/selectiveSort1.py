def sel_sort(a):
    n = len(a)
    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if a[j] < a[min_index]:
                min_index = j
        
        a[i], a[min_index]= a[min_index], a[i]

def sel_sort_ascend(a):
    n = len(a)
    for i in range(0, n-1):
        max_index = i
        for j in range(i+1, n):
            if a[j] > a[max_index]:
                max_index = j
        a[i], a[max_index] = a[max_index], a[i]


d = [2, 4, 5, 1, 3]

sel_sort(d)
print(d)
sel_sort_ascend(d)
print(d)
