from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        path = []

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                if crs not in path:
                    path.append(crs)
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            path.append(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return path
    
solution = Solution()

print(solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
