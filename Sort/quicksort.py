# Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

# Always pick first element as pivot.
# Always pick last element as pivot(implemented below)
# Pick a random element as pivot.
# Pick median as pivot.
# The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.


def quick_sort(a):
    n = len(a)

    if n <= 1:
        return a

    pivot = a[-1]
    g1 = []
    g2 = []

    for i in range(0, n-1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])

    return quick_sort(g1) + [pivot] + quick_sort(g2)


d = [6, 8, 3, 9, 10, 4, 1, 2, 7, 5]
print(quick_sort(d))
