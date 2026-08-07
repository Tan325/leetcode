class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        unique =[]
        l = 0
        for i in range (len(s)):
            if s[i] in unique:
                while unique[0] != s[i]:
                    unique.pop(0)
                unique.pop(0)
                unique.append(s[i])
                l = max(l, len(unique))
            else:
                unique.append(s[i])
                l = max(l, len(unique))

        return l
    
