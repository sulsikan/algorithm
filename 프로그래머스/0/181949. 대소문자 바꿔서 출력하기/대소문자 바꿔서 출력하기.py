str = input()
a=''

for s in str:
    if(s.isupper()):
        a += s.lower()
    else:
        a += s.upper()
        
print(a)