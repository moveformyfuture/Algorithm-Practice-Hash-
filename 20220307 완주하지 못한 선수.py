#1. 리스트의 '-' 연산 --> collections의 Counter 함수 사용
#2. Counter : 문자열이나 list의 요소를 카운팅하여, 많은 순으로 dic형태로 리턴한다.
#3. Counter : dic처럼 keys : values 형태로 자료형을 구성해줌
#4. Counter : 문자열의 '-'연산이 가능
#5. Counter는 list화 해줘야 함

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    return list(answer)[0]