class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i=0
        j=0
        count=0
        while(i<len(g) and j<len(s)):
            if j<len(s) and g[i]<=s[j]:
                count+=1
                j+=1
                i+=1
            elif g[i]>s[j]:
                j+=1
        return count
