from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported_cnt_list = defaultdict(int)
    report_list = [[] for _ in range(len(id_list))]
    
    for row in report:
        reporter, defendant = row.split()
        if defendant not in report_list[id_list.index(reporter)]:
            reported_cnt_list[defendant] += 1
            report_list[id_list.index(reporter)].append(defendant)
        
    for de in id_list:
        if reported_cnt_list[de] >= k:
            for re in id_list:
                if de in report_list[id_list.index(re)]:
                    answer[id_list.index(re)] += 1
        
        
    return answer