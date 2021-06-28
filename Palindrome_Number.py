class Solution:
    def isPalindrome(self, x: int) -> bool:
        value = str(x)
        reversed_value = value[::-1]
        for i in range(len(value)):
            if(value[i] != reversed_value[i]):
                return False
        return True


if __name__ == '__main__':
    candidates = [-121, 10, -101, 121]
    for c in candidates:
        answer = Solution().isPalindrome(c)
        print(answer)
