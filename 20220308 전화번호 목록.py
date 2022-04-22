# 동일 문자 비교 문제
# 1. phone_book을 오름차순으로 재구성한다 (sorted 사용)
# 2. 1번째 요소와 그 이후 요소를 index별로 짝을 맞춰준다. (hash)
# 3. 알파벳을 비교한다. (startswith)
# 4. True, False는 대문자로 사용

def solution(phone_book):
    phone_book = sorted(phone_book)  # sorted : 오름차순으로 list 재구성
    for a, b in zip(phone_book, phone_book[1:]):  # index 순으로 list 생성, index 수가 다르므로 모든 경우의수 반복함.

        if b.startswith(a):
            return False
        return True  # False가 아닌 경우 True 리턴