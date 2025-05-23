def solution(num_list):
    odd = []
    even = []
    
    for i in num_list:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    
    o = 0
    e = 0
    olen = len(odd)
    elen = len(even)
    num = 0
    
    for i in range(olen-1, -1, -1):
        o += odd[i] * 10**(num)
        num += 1
    
    num = 0
    for i in range(elen-1, -1, -1):
        e += even[i] * 10**(num)
        num += 1
    
    return o+e