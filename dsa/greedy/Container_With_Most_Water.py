class Solution:
    def maxArea(self, height: List[int]) -> int:
        #solution 3
        max_area = 0
        i=0
        j= len(height)-1
        while(i<j):
            k, l = i, j
            area1 = (j-i)*(min(height[j], height[i]))
            if height[i]>height[j]:
                j=j-1
            elif height[j]>height[i]:
                i=i+1
            else:
                i=i+1
                j=j-1
            max_area = max(area1, max_area)
            if k==i and l==j: break
        return max_area
