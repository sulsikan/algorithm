'''
2 -> 0
0 -> 5
5 -> 2

205 -> replace 052
'''
def solution(rsp):
    answer = ''
    tokens = [int(char) for char in rsp]
    
    for i in range(len(tokens)):
        if tokens[i] == 2:
            tokens[i] = 0
        elif tokens[i] == 0:
            tokens[i] = 5
        else:
            tokens[i] = 2
    answer = ''.join(str(digit) for digit in tokens)
    return answer