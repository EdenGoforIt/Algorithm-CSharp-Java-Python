# Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then it merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. See the following C implementation for details.

# MergeSort(arr[], l,  r)
# If r > l
#     1. Find the middle point to divide the array into two halves:
#             middle m = l + (r-l)/2
#      2. Call mergeSort for first half:
#            Call mergeSort(arr, l, m)
#      3. Call mergeSort for second half:
#            Call mergeSort(arr, m+1, r)
#      4. Merge the two halves sorted in step 2 and 3:
#            Call merge(arr, l, m, r)




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
