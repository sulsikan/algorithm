from itertools import permutations

def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))
    
def calculate(exp, op):
    array = []
    tmp = ''
    
    for e in exp:
        if e.isdigit():
            tmp += e
        else:
            array.append(tmp)
            array.append(e)
            tmp = ''
            
    array.append(tmp)
    
    for o in op:
        stack = []
        while array:
            tmp = array.pop(0)
            if tmp == o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(tmp)
        array = stack
        
    return abs(int(array[0]))

def solution(expression):
    op = ['+', '-', '*']
    op = list(permutations(op, 3))
    result = []
    
    for op_list in op:
        result.append(calculate(expression, op_list))
        
    return max(result)