class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                k = 0
                str_1 = nums[j]+nums[j+1]
                str_2 = nums[j+1] + nums[j]
                while(k<len(str_1) and int(str_1[k]) == int(str_2[k])):
                    k = k+1    
                if ( k<len(str_1) and int(str_1[k]) < int(str_2[k])):
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
                
        
        s = ""
        for i in range(len(nums)):
            s = s+ nums[i]
        k=0
        while k<len(s) and s[k]=="0":
            k=k+1
        if k!=0: s = s[k-1:]

        
        return s
