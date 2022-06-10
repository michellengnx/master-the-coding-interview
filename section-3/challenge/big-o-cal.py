# Section 3 - Big O Calculation

# Challenge 1
# The below funChallenge function has O(n) - linear time complexity

def anotherFunction():
    print('anotherFunction')


def funChallenge(input):
    x = 10
    a = 50 + 3
    for x in input:
        anotherFunction()
        stranger = True
        a = a + 1
    return a


# Challenge 2
# The below funChallenge function has O(n) - linear time complexity

def anotherFunChallenge(input):
    # 3 -> the operation is INDEPENDENT of the input
    a = 5
    b = 10
    c = 50
    # 3n
    for i in input:
        x = i + 1
        y = i + 2
        z = i + 3
    # 2n
    for j in input:
        p = j * 2
        q = j * 2
    # 1
    whoAmI = "I don't know"

#

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
