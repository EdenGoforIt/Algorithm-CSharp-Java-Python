import datetime
from typing import List


class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC',
                  'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        answer = ''
        i = 0
        while num:
            answer += num//values[i]*romans[i]
            num = num % values[i]
            i += 1
        return answer


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    # for i in range(10):
    test = Solution().intToRoman(1994)
    print(test)

    end_time = datetime.datetime.now()
    diff = int((end_time - start_time).total_seconds()*1000)
    print("Execution time: {} ".format(diff))
