class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
   
        res = 0
        dp = []

        for i in range(len(gas)):
            res = res + gas[i] - cost[i]
            dp.append(gas[i]-cost[i])
        if res<0: return -1
        s=0
        index=0
        a=1
        b=-1
        for i in range(len(dp)):
            s+=dp[i]
            if s<0:
                s=0
                index=i+1
        return index
