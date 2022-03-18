#C問題の復習
import bisect #二分探索を効率良く行うためのライブラリ

n,q= map(int,input().split())
a = list(map(int,input().split()))
a.sort()#探索するリストをソートする

ans = []
for i in range(q):
    ans.append(int(input()))
print()
for i in range(q):
    #a -->探索元のリスト
    #ans[i] --> 挿入する要素
    A = bisect.bisect_left(a,ans[i])
    #ans[i]を挿入した場所(index)を返す
    #ans[i]を挿入した場所がa[n-1]ならaリストの中に条件を満たす要素がない
    #ans[i]を挿入した場所がa[0]~a[n-2]の範囲なら条件を満たす要素あり
    print(n-A)