n = int(input())

a = []

for _ in range(n):
    s, p = input().split()
    a.append((s, int(p)))
#ラムダ関数を使って市名を昇順に、点数が降順になるようにソート
#ラムダ関数はsoretd()の引数に使われたりする
b = sorted(a, key=lambda x: (x[0], -x[1]))