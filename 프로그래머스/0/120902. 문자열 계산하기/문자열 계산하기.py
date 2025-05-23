def solution(my_string):
    tokens = my_string.split()
    result = int(tokens[0])
    
    for i in range(1, len(tokens), 2):
        op = tokens[i]
        num = int(tokens[i+1])
        
        if op == '+':
            result += num
        else:
            result -= num
            
    return result