from collections import Counter
from functools import reduce
def solution(clothes):
    # 1. 의상을 종류별로 분류한다.
    counter=Counter([type for clothe, type in clothes]) # Counter에는 list를 해줘야함

    # 2. 모든 종류의 count+1을 누적해서 곱해준다.
    answer = reduce(lambda acc, cur : acc * (cur+1), counter.values(),1)
    # lambda : acc와 cur이 있을 때 acc * (cur+1)를 수행하겠다.
    # cur의 값은 counter.values()로 지정, 그 초기값은 1로 지정

    return answer-1
