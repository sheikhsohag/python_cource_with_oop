n,m = input().split()
n =int(n)
m = int(m)

arr = list(map(int, input().split()))
fre = {}
for i in range(1,m+1):
    fre[i]=0

for item in arr:
    fre[item]+=1


for i in sorted(fre.keys()):
    print(fre[i])