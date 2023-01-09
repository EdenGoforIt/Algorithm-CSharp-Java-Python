def longest_palindrome(s):
    if not s:
        return ''
    longest = ''
    for i in range(len(s)):
        # odd case, like “aba”
        tmp = middle_out(s, i, i)
        if len(tmp) > len(longest):
            # update the res
            longest = tmp
        # even case, like “abba”
        tmp = middle_out(s, i, i+1)
        if len(tmp) > len(longest):
            longest = tmp
    return longest


def middle_out(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1  # decrement the left
        r += 1  # increment the right
    return s[l+1:r]

answer = longest_palindrome("cbba");