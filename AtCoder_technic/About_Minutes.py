#自然数Nを約分できる数字がいくつ含まれているかを調べる

#計算量が小さいので全探索する
#1以上～n+1以下の奇数のうち約数をちょうど8個持つものを調べる
n = int(input())
cnt_sum = 0
for i in range(1,n+1,2):#約分する数字は
    cnt = 0
    for j in range(1,n+1):
        if i % j == 0:
            cnt += 1
        print(i%j,cnt)

    if cnt == 8:
        cnt_sum += 1
print(cnt_sum)