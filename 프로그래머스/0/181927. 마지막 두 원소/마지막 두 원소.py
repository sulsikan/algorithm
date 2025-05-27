'''
if num_list[n-1] < num_list[n]:
return num_list.append(num_list[n] - num_list[n-1])

else:
return numlist.append(num_list[n] * 2)
'''
def solution(num_list):
    
    N = len(num_list)
    if num_list[N-2] < num_list[N-1]:
        num_list.append(num_list[N-1] - num_list[N-2])
    else:
        num_list.append(num_list[N-1] * 2)
        
    return num_list