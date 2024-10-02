import math

class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while(n!=1):
            while n%2==0:
                count+=1
                n=n/2
            if n!=1 and n!=3 and int((n+1)/2)%2==0:
                n=n+1
            elif n!=1:
                n=n-1
            if n==1:return count
            count+=1
        return count
