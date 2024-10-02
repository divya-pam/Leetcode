class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        p=0
        b=None
        s=None
        for i in range(len(prices)):
            if b==None and i+1<len(prices)and prices[i]<prices[i+1]:
                b=prices[i]
            if b!=None and prices[i]>b and prices[i]-b>=m:
                m=prices[i]-b
                s=prices[i]
                if i==len(prices)-1: p+=m
                print(m)
            if s!=None and prices[i]<s:
                b=prices[i]
                p+=m
                print('m ', m)
                m=0
        #if b!=None and prices[-1]-b>m: p+=prices[-1]-b
        return p
