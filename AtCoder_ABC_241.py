s = list(input())
S = sorted(s)
ans = ""
for i in range(len(S)):
    ans = ans +  S[i]
print(ans)