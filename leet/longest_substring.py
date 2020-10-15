class Solution:
    def if_duplicate(self,s,c):
        if(s.count(c)>0):
            return True
        else:
            return False

    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==1):
            return 1
        res = 0
        for x in range(len(s)):
            for j in range(x,len(s)):
                if(self.if_duplicate(s[x:j],s[j])):
                    res = max(res,j-x)
                    break
                else:
                    res = max(res,j-x+1)
        return res
    
