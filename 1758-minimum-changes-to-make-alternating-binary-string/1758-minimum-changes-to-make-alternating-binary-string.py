class Solution:
    def minOperations(self, s: str) -> int:
        cost1 = 0 #expects 010101...
        cost2 = 0 #expects 101010...
        
        for i in range(len(s)):
            if i%2 == 0:
                if s[i] == '0':
                    cost2 += 1
                else:
                    cost1 += 1
            else:
                if s[i] == '0':
                    cost1 += 1
                else:
                    cost2 += 1
                    
        return min(cost1, cost2)