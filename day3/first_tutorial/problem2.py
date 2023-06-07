nn=input()
n=int(nn)
a = list(map(int,input().strip().split()))

vis={}
ans=0
ab=0
for i in a:
    if i in vis:
        vis[i]=vis[i]+1;
    else:
        vis[i]=1;

ans=0
for k, value in vis.items():
    if k>value:
        ans+=value
    else:
        ans+=value-k
print(ans)




