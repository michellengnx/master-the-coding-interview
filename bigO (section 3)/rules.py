# Big O rules
# Rule 1: always assume worst case
# Rule 2: remove constant
# Rule 3: different term for input

def compressBoxesTwice(boxes1, boxes2):
    for box in boxes1:
        print(box)
    for box in boxes2:
        print(box)

# -> Big 0 for the above function is O(n + m)

# Rule 4: drop non-dominant terms

