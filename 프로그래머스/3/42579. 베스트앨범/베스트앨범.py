from collections import defaultdict

def solution(genres, plays):
    
    # 장르별 총 재생수
    genre_total = defaultdict(int)
    # 장르별 노래 저장
    genre_song = defaultdict(list)
    
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        
        genre_total[g] += p
        # (재생수, 고유번호)
        genre_song[g].append((p, i))
    
    
    # 장르 총 재생수 기준 정렬
    sorted_genre = sorted(
        genre_total.items(),
        key=lambda x: x[1],
        reverse=True
    )
    
    answer = []
    
    for g, _ in sorted_genre:
        
        # 재생수 내림차순
        # 같으면 번호 오름차순
        songs = sorted(
            genre_song[g],
            key=lambda x: (-x[0], x[1])
        )
        
        # 최대 2개
        for song in songs[:2]:
            answer.append(song[1])
    
    return answer