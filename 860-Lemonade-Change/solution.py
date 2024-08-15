from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveBills, tenBills = 0, 0
        
        for i in bills:
            if i == 5:
                fiveBills += 1
            elif i == 10:
                if fiveBills == 0:
                    return False
                fiveBills -= 1
                tenBills += 1
            else:
                if tenBills > 0 and fiveBills > 0:
                    tenBills -= 1
                    fiveBills -= 1
                elif fiveBills >= 3:
                    fiveBills -= 3
                else:
                    return False
        
        return True

    
print(Solution().lemonadeChange([5,5,5,10,20]))