    def unique_paths(m, n):
        if m==0 or n==0:
            return 1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1 
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

    def unique_paths(m, n):
        if m==0 or n==0:
            return 1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        def find_paths(dp, i, j):
            if i==0 or j==0:
            return 1
            if dp[i][j]!=-1: return dp[i][j]
            dp[i][j] = find_paths(dp, i-1, j) + find_paths(dp, i, j-1)
            return dp[i][j]

        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1 
        return find_paths(dp, m-1, n-1)
