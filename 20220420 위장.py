
def solution(clothes):
    # 1. 옷을 종류별로 구분하기
    hash_map={} # dic 정의
    for clothe, type in clothes :
        hash_map[type] = hash_map.get(type,0)+1 # get : hash_map에서 type을 가져오고, 없으면 0을 가져옴

    # 2. 입지 않는 경우를 추가해서 모든 조합을 계산하기
    answer=1
    for type in hash_map:
        answer *= (hash_map[type]+1)

    # 3. 아무 종류의 옷도 입지 않는 경우를 제외한다.
    return answer-1