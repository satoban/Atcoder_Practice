#B問題
n = int(input())
w = list(map(int,input().split()))

n = n - 1
x = w[n//2]
y = w[(n//2)+1]

ans = 101
for i in range(x):
    for j in range(y,n):
        ans = min(ans,abs(i-j))
print(ans)