class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            degree = ord('z') - ord(s[i]) + 1
            res += degree * (i + 1)
        
        return res
        
