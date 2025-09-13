
    def rob_houses(houses):
        if len(houses) == 0: return 0
        elif len(houses) == 1: return houses[0]
        dp = [houses[0],houses[1],]
        for i in range(2, len(houses)):
            dp[i] = max(houses[i] + dp[i-2], dp[i-1])
        return dp[len(houses)-1]
    

    def rob_houses(houses):
        if len(houses) == 0: return 0
        elif len(houses) == 1: return houses[0]
        dp = -1*(len(houses)+1)
        dp[0] = houses[0]
        dp[1] = houses[1]
        def find_price(i, dp):
            if i<=1:
                return dp[i]
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(find_price(i-2, dp) + houses[i], find_price(i-1, dp))
            return dp[i]
        find_price(len(house), dp)
