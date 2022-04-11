"""
以下の条件で貪欲法を用いて解いていく
1.全商品がx円未満になるまでクーポンを使う
2.全商品がx未満になったら、価格が高い順にクーポンを使って0円にする
"""
n,k,x = map(int,input().split())
#n個の商品、k枚のクーポン、xは割引額
A = list(map(int,input().split()))
ans = sum(A)
rem = k
Q = 0
R =[]
#Qはx円引きできる回数を求めている
#Rはx円引きし終わった後の余りを大きい順に並べる
for a in A:
    Q += (a//x)
    R.append(a%x)
#sort()は元のリストを書き換える破壊的処理の為、Noneを返す
#sorted()は元のリストを保持したままソートした新しいリストを作成する非破壊的処理
R = sorted(R,reverse=True)
#Qとクーポンの枚数の少ないほうだけx円引きできる
ans -= x * min(Q,rem)
#x円引きに使った分クーポンを減らす
rem -= min(Q,rem)
#残りのクーポンを余りの大きい順に使う(スライスは例外参照をおこさないので,indexがデカくなっても大丈夫)
ans -= sum(R[:rem])
print(ans)