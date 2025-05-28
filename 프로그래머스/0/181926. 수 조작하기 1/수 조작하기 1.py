'''
n, control(w 1,a -10,s -1,d 10)
1. list(control)
2. for i in len(con):
        if con[i] == 'w':
            n+=1
'''
def solution(n, control):
    con = list(control)
    for i in range(len(con)):
        if con[i] == 'w':
            n+=1
        elif con[i] == 's':
            n-=1
        elif con[i] == 'd':
            n+=10
        else:
            n-=10
    return n