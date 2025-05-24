'''
다른 풀이 : 딕셔너리로 매핑
'''
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)