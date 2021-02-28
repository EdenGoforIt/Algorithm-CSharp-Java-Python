
def longestPalindrome(s: str) -> str:
    if(len(s) == 1):
        return s
    answer = ''
    for i in range(len(s)):
        for j in range(len(s)):
            if i > j:
                continue
            partial = s[i:j]
            reversed_partial = s[i:j][::-1]
            if abs(i-j) <= len(answer):
                continue
            elif(s[i:j] == s[i:j][::-1]):
                answer = s[i:j] 
    return answer


if __name__ == "__main__":
    print(longestPalindrome("babad"))
    print(longestPalindrome("cbbd"))
    print(longestPalindrome("a"))


# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
# Example 3:

# Input: s = "a"
# Output: "a"
# Example 4:

# Input: s = "ac"
# Output: "a"
