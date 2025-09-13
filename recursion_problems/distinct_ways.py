    def distinct_ways(n):
        if n<=0:
            return 0
        elif n<=2:
            return 2
        dp = [0,1,2,]
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
            
    def distinct_ways(n, memo):
        if n == None:
            return (0,memo)
        elif n<=2:
            return (2, memo)
        if memo == None:
            memo = [0,1,2]
        memo[n] = distinct_ways(n-1) + distinct_ways(n-2)
        return (memo[n], memo)
