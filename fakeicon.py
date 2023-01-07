def weigh(a, b, c, d):
    fake = 29
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0

def find_fake_coin(left, right):
    for i in range(left+1, right +1):
        result = weigh(left, left, i, i)

        if result == -1:
            return left
        elif result == 1:
            return i
    
    return -1

