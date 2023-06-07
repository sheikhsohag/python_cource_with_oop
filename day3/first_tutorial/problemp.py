ans = 1000

n=int(input())

ar=list(map(int,input().split()))

for i in ar:
    b=i
    cnt=0
    while b%2==0:
        cnt+=1
        b/=2
    if cnt<ans:
        ans=cnt
print(ans)

