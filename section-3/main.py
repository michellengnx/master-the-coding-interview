# Section 3 - Big O Calculation - Challenge 1
# The below funChallenge function has O(n) - linear time complexity

def anotherFunction():
    print('anotherFunction')
def funChallenge(input):
    x = 10
    a = 50 + 3
    for x in input:
        anotherFunction()
        stranger = True
        a=a+1
    return a
if __name__ == '__main__':
    funChallenge('Michelle')

#

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
