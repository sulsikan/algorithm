from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report_cnt = [0] * len(id_list)
    report_log = [[] for _ in range(len(id_list))]
    
    for row in report:
        re, de = row.split()
        
        if de not in report_log[id_list.index(re)]:
            report_cnt[id_list.index(de)] += 1
            report_log[id_list.index(re)].append(de)
        
    for i in range(len(id_list)):
        re_cnt = 0
        for de_log in report_log[i]:
            if report_cnt[id_list.index(de_log)] >= k:
                re_cnt += 1
        answer.append(re_cnt)
        
    return answer