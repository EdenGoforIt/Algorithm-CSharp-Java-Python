def findMedian(arr):

    half = len(arr) // 2
    arr.sort()
    if not len(arr) % 2:
        return (arr[half - 1] + arr[half]) / 2.0
    return arr[half]

    sorted_arr = sorted(arr)
    length = len(arr)

    index = int(length / 2)
    return sorted_arr[index]


if __name__ == '__main__':
    print(findMedian([1, 2, 3]))
    print(findMedian([1, 2, 3, 4]))
