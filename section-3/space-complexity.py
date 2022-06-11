#Space complexity

def sayBoooo(n):
    for x in n:
        print('boooo');

sayBoooo([1,2,3,4,5])

# Space complexity of an algorithm is the total space taken by the algo with respect to input size
# Do not include space of  the input when calculating space complexity
# Space complexity of the above function is O(n)

def sayHiMultipleTimes(n):
    hiArray = []
    for i in n:
        hiArray.append('Hi')
    return hiArray

hiArray = sayHiMultipleTimes([1,2,3,4,5])
print(hiArray)

# Space complexity of the above function is O(n). More space is required if input size gets larger





