#AtCoder　B問題　
""" 
defaultdictを使うことで存在しないキーが出現しても、エラーが出ない。
また、キーが無い場合は新しい要素を追加してくれる。
"""
from collections import defaultdict
s =  input()

ans = defaultdict(int)

for i in range(len(s)):
    ans[s[i]] += 1
"""
上のfor文は文字列をansのindexにすることでそれぞれの文字が出現した時、カウントする仕組みとなっている。
"""
if len(s) == len(ans):
    print("yes")
else:
    print("no")