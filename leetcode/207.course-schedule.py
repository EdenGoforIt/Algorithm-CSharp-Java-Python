#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build graph
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            print("course:", course, "prereq:", prereq)
            graph[prereq].append(course)
            # How many prerequisites this course has
            in_degree[course] += 1

        
        print(in_degree)
        print(graph)
        return True


# @lc code=end

print(Solution().canFinish(2, [[1, 0], [0, 1]]))  # Example test case
