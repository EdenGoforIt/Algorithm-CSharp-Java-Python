def weigh(a, b, c, d):
    fake = 29
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0


def find_fake_coin(left, right):
    for i in range(left+1, right + 1):
        result = weigh(left, left, i, i)

        if result == -1:
            return left
        elif result == 1:
            return i

    return -1


def find_fake_coin2(left, right):
    if left == right:
        return left

    half = (right - left+1)//2  # 2, 5 = 5-2+1 = 1
    g1_left = left  # 2
    g1_right = left + half - 1  # 2 + 1 -1 = 2
    g2_left = left + half  # 2 + 1 = 3
    g2_right = right
    result = weigh(g1_left, g1_right, g2_left, g2_right)
    if result == -1:
        return find_fake_coin2(g1_left, g1_right)
    elif result == 1:
        return find_fake_coin2(g2_left, g2_right)
    else:
        return right


print(find_fake_coin(0, 100-1))
