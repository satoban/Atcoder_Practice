#ABC242_C問題
#動的計画法（DP）法
MOD =99824453

N = int(input())

dp = [ [0] * 9 for _ in range(N)]
dp[0] = [1] * 9
print(dp)
print()
for i in range(1,N):#1~N
    for d in range(9):#0~8
        print(dp)
        if d -1 >= 0:
            print(str(dp[i-1][d-1])+"!")
            dp[i][d] += dp[i-1][d-1]
            print(str(dp[i][d])+"!,")

        dp[i][d] += dp[i-1][d]
        print(str(dp[i][d]))

        if d + 1 < 9:
            print(str(dp[i-1][d+1])+"?")
            dp[i][d] += dp[i-1][d+1]
            print(str(dp[i][d])+"?,")

        dp[i][d] %= MOD 
        print(str(dp[i][d])+"@")
print(sum(dp[N-1]) % MOD)
print(dp)