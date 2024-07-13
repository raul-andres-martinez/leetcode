from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for c in range(1, len(strs)):
                if i == len(strs[c]) or strs[0][i] != strs[c][i]:
                    return strs[0][:i]
        return strs[0]


print(Solution().longestCommonPrefix(["flower","flow","flight"]))