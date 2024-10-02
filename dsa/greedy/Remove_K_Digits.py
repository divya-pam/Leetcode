import sys
sys.set_int_max_str_digits(10000)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k==len(num): return str(0)
        dp = []
        m=[str(9999999)]
        def remove(s, k, dp, m):
            if k==0 :
                if int(s)<int(m[0]):
                    print('here')
                    m[0] = s
                return 
            for i in range(0, len(s)):
                st = s[:i] + s[i+1:]
                remove(st, k-1, dp, m)
            return 
        remove(num, k, dp, m)
        return str(int(m[0]))
        m = 9999999
        #print(dp)
        for i in range(len(dp)):
            if m>int(dp[i]):
                m=int(dp[i])
        return str(m)
