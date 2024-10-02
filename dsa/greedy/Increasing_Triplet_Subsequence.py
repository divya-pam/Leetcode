class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mi = nums[0]
        se_mi = 99999999
        ma = nums[-1]
        for i in range(1, len(nums)):
            
            if se_mi ==99999999 and nums[i]>mi: se_mi = nums[i]
            elif nums[i]>mi and nums[i]<se_mi:
                se_mi = nums[i]
            elif nums[i]>se_mi: 
                return True
            elif ma>se_mi and ma>mi and mi<se_mi:
                return True
            elif nums[i]<mi and nums[i]<ma:
                se_mi = 99999999
                mi = nums[i]
            if nums[len(nums)-i]>ma: ma = nums[len(nums)-i]
        return False
            


        min_arr = [nums[0], ]
        max_arr = [nums[len(nums)-1]]
        for i in range(1,len(nums)):
            min_arr.append(nums[i-1] if nums[i-1]<min_arr[-1] else min_arr[-1])
            max_arr.append(nums[len(nums)-i] if nums[len(nums)-i]>max_arr[-1] else max_arr[-1])
        max_arr = max_arr[::-1]
        for i in range(1, len(nums)):
            if nums[i]>min_arr[i] and nums[i]<max_arr[i]:
                return True
        return False
