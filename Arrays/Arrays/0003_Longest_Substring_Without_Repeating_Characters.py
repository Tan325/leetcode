class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        count = 0 
        new = ""
        for i in range(len(s)):
            for j in range(i):
                if s[i] not in new:
                    new += s[i]
    
        return len(new)