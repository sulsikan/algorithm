n=int(input())
s=list(map(int, input().split()))
b, c = map(int, input().split())
res=0

for i in range(n):
    s[i] -= b
    res+=1
    
    if s[i]>0:
        if s[i]%c==0:
            res += s[i]//c
        else:
            res += (s[i]//c +1)
print(res)