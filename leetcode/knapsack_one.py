# from typing import List
# Ollie came to the gym for the first time, and she was calculating the maximum weight she could lift. The maximum weight that a barbell can bear is maxCapacitythat there are n bars in the gym, and the weight of the i-th barbell is weights[i]. Ollie now needs to choose some barbells to add to the barbell to maximize the weight of the barbell, but the total weight of the selected barbells cannot exceed maxCapacity. Please calculate the maximum weight of the barbell.

# For example, given the weight of the barbell plate is weights = [1, 3, 5], and the maximum weight of the barbell is maxCapacity = 7, then barbell plates with weights 1 and 5 should be selected, (1 + 5=6), so The final answer is 6.


# this solution is a brute force, which is  n^2 time.

from typing import List
import datetime


class Solution:
    def kapsack(self, nums: List[int], k: int) -> int:
        size = len(nums)
        max_capacity = k
        weights = [False] * (max_capacity+1)
        weights[0] = True
        for i in range(0, len(nums), 1):
            initial_value = nums[i]
            temp = nums[i]
            for j in range(0, len(nums), 1):
                potential_total = temp + nums[j]
                if (initial_value is not nums[j]) and ((temp + nums[j]) < max_capacity) and weights[potential_total] is False:
                    temp += nums[j]
                    weights[potential_total] = True

        biggest = 0
        for index in range(len(weights) - 1, 0, -1):
            if weights[index] is True:
                biggest = index
                break

        return biggest


if __name__ == '__main__':
    start_time = datetime.datetime.now()

    nums = [9, 3, 5, 7]
    k = 15
    test = Solution().kapsack(nums, k)
    print(test)
    end_time = datetime.datetime.now()
    diff = int((end_time - start_time).total_seconds()*1000)
    print("Execution time: {} ".format(diff))
