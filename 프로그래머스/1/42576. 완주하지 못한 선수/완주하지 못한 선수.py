from collections import defaultdict

def solution(participant, completion):
    players = defaultdict(int)
    for p in participant:
        players[p] += 1
    for c in completion:
        players[c] -= 1
    return max(players, key=players.get)