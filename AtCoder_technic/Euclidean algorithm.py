#ユークリッドの互除法
A,B = map(int,input().split())
a = A
b = B
mod = 0
while True:
    if a > b:
        a = a%b
    elif b > a:
        b = b%a
    print(a,b)
    if a==0:
        print(A*B//b)
        exit()
    if b==0:
        print(A*B//a)
        exit()