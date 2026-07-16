def solution(dirs):
    answer = 0
    path = [[] for _ in range(len(dirs)+1)]
    path[0] = [5, 5]
    start = [5, 5]
    visited = []
    
    for i in range(0, len(dirs)):
        
        if dirs[i] == 'U':
            path[i+1] = [path[i][0], path[i][1]+1]       
        elif dirs[i] == 'D':
            path[i+1] = [path[i][0], path[i][1]-1]
        elif dirs[i] == 'R':
            path[i+1] = [path[i][0]+1, path[i][1]]
        else:
            path[i+1] = [path[i][0]-1, path[i][1]]
            
        if 0 <= path[i+1][0] < 11 and 0 <= path[i+1][1] < 11:
            chk_p = [start[0], start[1], path[i+1][0], path[i+1][1]]
            
            if chk_p not in visited:
                print(chk_p)
                visited.append(chk_p)
                visited.append([path[i+1][0], path[i+1][1], start[0], start[1]])
                answer += 1
        
            start = [path[i+1][0], path[i+1][1]]
            
        else:
            path[i+1] = path[i]
    
    return answer