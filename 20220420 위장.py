# 1. hash_map을 만들기.
# 2. 종류별로 묶어 곱해주기
# 3. 아무것도 입지 않는 경우 빼주기 (예외처리)

def solution(clothes):
    hash_map = {}

    for name, kind in clothes:
        hash_map[kind] = hash_map.get(kind, 0) + 1  # get(key) : key에 해당하는 value를 반환
        # dict가 선언되지 않았으므로, 0부터 value 값을 하나씩 누적해나감

    answer = 1
    for kind in hash_map:
        answer *= (hash_map[kind] + 1)

    return answer - 1