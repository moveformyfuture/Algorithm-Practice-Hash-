import collections # Counter 함수를 쓰기 위해 호출

def solution(participant, completion):
    answer = collections.Counter(participant)-collections.Counter(completion) # Counter() : dic처럼 key와 value로 만들어줌
                                                                              # Counter() 를 사용해야 객체끼리 빼기 연산 가능
    return list(answer.keys())[0] # keys()함수 사용해 key만 호출, list화해서 남아있는 key 반환