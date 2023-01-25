n,k=map(int,input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
count=0

for i in range(n):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
        count+=1
    if count==3:
        break
print(sum(a))

#풀이
n,k=map(int,input().split())
c=list(map(int, input().split()))
d=list(map(int, input().split()))
c.sort()
d.sort(reverse=True)

for i in range(k):
    if c[i]<d[i]:
        c[i],d[i]=c[i],d[i]
    else:
        break
print(sum(c))
