class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums)==0: return nums
        maximum = nums[0]
        minimum = nums[-1]
        s=0
        e=0
        array_pre = 0
        for i in range(1, len(nums)):
            if nums[i]<maximum: e=i
            if nums[i]>maximum: maximum = nums[i]
        for i in range(len(nums)-2, -1, -1):
            if nums[i]>minimum: s=i
            if nums[i]<minimum: minimum = nums[i]
        return e-s+1 if e!=0 else 0
