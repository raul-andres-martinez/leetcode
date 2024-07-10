from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth: int = 0
        for i in logs:
            if i == "../":
                if depth > 0:
                    depth -= 1
            elif i != "./":
                depth += 1

        return depth