class Solution:
    def jump(self, nums: List[int]) -> int:
        dp=[]
        for i in range(len(nums)):
            dp.append(999999999)
        dp[-1] = 0
        for i in range(len(nums)-2, -1, -1):
            for j in range(i, i+nums[i]+1):
                if j<len(nums): dp[i] = min(dp[i], 1+dp[j])
        return dp[0]
