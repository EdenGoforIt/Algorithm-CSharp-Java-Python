
def find_index(result, value):
    for i in range(0, len(result)):
        if result[i] > value:
            return i

    return len(result) 

def insert_sort(list):
    result = []
    while list:
        value = list.pop(0)
        index = find_index(result, value)
        result.insert(index, value)

    return result


list = [3, 5, 1, 2, 9]
print(insert_sort(list))
