
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
devices = list(map(int, input().split()))
multitap = [0] * n
replace_count = 0

while devices:
    now_device = devices.pop(0)
    # multitap check
    if now_device in multitap:
        continue
    else:
        # empty check
        if 0 in multitap:
            for i in range(n):
                if multitap[i] == 0:
                    multitap[i] = now_device
                    break
        # replace
        else:
            candidate_idx = -1
            candidate_device = multitap[0]
            break_flag = False
            for i in range(n):
                if multitap[i] not in devices:
                    multitap[i] = now_device
                    replace_count += 1
                    break_flag = True
                    break
                else:
                    next_use = devices.index(multitap[i])
                    if next_use > candidate_idx:
                        candidate_idx = next_use
                        candidate_device = multitap[i]
                        
            if not break_flag:
                multitap[multitap.index(candidate_device)] = now_device
                replace_count += 1

print(replace_count)
