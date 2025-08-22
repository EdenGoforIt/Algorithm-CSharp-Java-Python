#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
from collections import defaultdict, deque
from typing import List


# @lc code=start
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build prerequisite graph
        graph = defaultdict(list)

        # Number of prerequisites
        # if math 1 and math 2 can be followed by common math
        # e.g [0, 1, 1] 0 -> common math, math 1 -> 1, math 2 ->1
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            # 0 -> [1,2] common math is pre requisite for math 1, 2
            graph[prereq].append(course)
            in_degree[course] += 1

        # Initialize queue with courses having no prerequisites
        # Common math [0] will be in the queue as it doesn't have any prerequisites
        # queue -> [0] common math
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited = 0

        while queue:
            curr = queue.popleft()
            visited += 1
            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If all courses are visited, it's possible to finish all
        return visited == numCourses


# @lc code=end

print(Solution().canFinish(2, [[1, 0]]))  # Example test case
