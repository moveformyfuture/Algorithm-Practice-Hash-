def solution(clothes):
    from collections import Counter # list의 더하기 빼기
    from functools import reduce #
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer