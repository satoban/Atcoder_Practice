#各桁の和を求める関数

#各桁の合計値を計算をする関数
def digitSum(x):
  #仮引数に受け取った値を文字列に変換
  x = str(x)
  #文字列を1文字ずつ数値化し配列にする
  array = list(map(int,x))
  #合計値を返す
  return sum(array)