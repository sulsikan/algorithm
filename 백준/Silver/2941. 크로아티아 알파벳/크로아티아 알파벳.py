
word = input()
croatia_alphabets = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for c in croatia_alphabets:
    word = word.replace(c,'*')
    
print(len(word))