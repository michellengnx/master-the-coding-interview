def merge_sorted_arrays(array1: object, array2: object) -> object:
    if len(array1) == 0 or len(array2) == 0:
        return array1 + array2
    i = 0
    j = 0
    new_array = []

    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            new_array.append(array1[i])
            i = i + 1
        elif array2[j] < array1[i]:
            new_array.append(array2[j])
            j = j + 1
    return new_array + array1[:i] + array2[:j]


a = [1, 3, 4]
b = [2, 6, 7]
newArray = merge_sorted_arrays(a, b)
print(newArray)
