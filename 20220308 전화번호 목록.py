def solution(phoneBook):
    phoneBook = sorted(phoneBook) # sorted : 새로운 정렬된 iterable 리스트로 만들어 반환

    for p1, p2 in zip(phoneBook, phoneBook[1:]): # zip() : 함수 안의 리스트, 튜플, 문자열에 대해 각 요소를 index 순으로 짝지어 주는 함수
                                                 # zip 하면 앞글자에 맞추어 정렬이 됨
                                                 # 반환값이 list가 아니기 때문에 for문에 대입하는게 아니라면 list 처리 해줘야함
                                                 # index가 0부터 시작하지 않으므로 모든 경우의 수를 반복함
        if p2.startswith(p1): # startswith : p2가 p1로 시작하면 True, 그렇지 않으면 False 반환
                              # 두 매개변수 중 뒤에것과 앞에것의 일치 여부를 비교
            return False
    return True