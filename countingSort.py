def countingSort(arr):
    result = [0]*100
    for i in range(len(arr)):
        index = arr[i]
        result[index] += 1
    return result


if __name__ == '__main__':
    print(countingSort([1, 1, 3, 2, 1]))
