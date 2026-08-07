class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        new =""
        p_l =[]
       
        for k in range (len(s)):
            new = ""
            for i in range(k,len(s)):
               new += (s[i])
               if new == new[::-1]:
                   p_l.append(new)
        
        
        longest = max(p_l, key = len)
        return longest
