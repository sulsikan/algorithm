import sys
input = sys.stdin.readline

word = input().strip()
croatia_alphabet = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for c in croatia_alphabet:
        word = word.replace(c, "*")

print(len(word))