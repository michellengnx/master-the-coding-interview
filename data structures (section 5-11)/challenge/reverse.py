def reverse(str):
    result = ""
    for i in range(len(str) - 1, -1, -1):
        result = result + str[i]
    return result


result = reverse('Hi I am Michelle')

print(result)
