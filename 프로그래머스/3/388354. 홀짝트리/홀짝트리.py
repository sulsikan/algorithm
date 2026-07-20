from collections import defaultdict
    
def check_node(table, start, visited, stats):
    stack = [start]
    visited.add(start)

    while stack:
        node = stack.pop()

        if node % 2 == 1 and len(table[node]) % 2 == 1:
            stats[0] += 1
        if node % 2 == 0 and len(table[node]) % 2 == 0:
            stats[1] += 1
        if node % 2 == 1 and len(table[node]) % 2 == 0:
            stats[2] += 1
        if node % 2 == 0 and len(table[node]) % 2 == 1:
            stats[3] += 1

        for nxt in table[node]:
            if nxt not in visited:
                visited.add(nxt)
                stack.append(nxt)
    return
    
def solution(nodes, edges):
    answer = [0, 0]
    
    tables = defaultdict(set)
    
    for n1, n2 in edges:
        tables[n1].add(n2)
        tables[n2].add(n1)
    
    visited = set()
    
    
    for node in nodes:
        if node in visited:
            continue
            
        stats = [0, 0, 0, 0]
        check_node(tables, node, visited, stats)
            
        if stats[0] + stats[1] == 1:
            answer[0] += 1
        if stats[2] + stats[3] == 1:
            answer[1] += 1
    
    return answer