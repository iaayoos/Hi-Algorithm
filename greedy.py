N=int(input())
plans=input().split()
x,y=1,1

dx=[0,0,1,-1]
dy=[1,-1,0,0]
d=['R','L','D','U']

for plan in plans:
    for i in range(4):
        if plan==d[i]:
            mx=dx[i]
            my=dy[i]
    if (1>x+mx) or (x+mx>N) or (1>y+my) or (y+my>N):
        continue
    x+=mx
    y+=my

print(x,y)
