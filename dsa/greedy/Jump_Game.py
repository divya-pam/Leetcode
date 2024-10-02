class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = []
        s=0
        for i in range(len(nums)):
            dp.append(0)
        dp[len(nums)-1]=0
        j=len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i]+i>=j:
                dp[i]=1+dp[j]
                j=i
                s=s+1

        if nums[0]<j:
            return False
        
        return True
