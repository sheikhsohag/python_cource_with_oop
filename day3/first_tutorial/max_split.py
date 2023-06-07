ss=input()
#print(ss)

LL=0
RR=0
ans_ss=''
ans=[]

for i in ss:
    ans_ss+=i
    if i=='L':
        LL+=1
    else:
        RR+=1
    
    if LL==RR:
        ans.append(ans_ss)
        ans_ss=''

print(len(ans))
for i in ans:
    print(i)