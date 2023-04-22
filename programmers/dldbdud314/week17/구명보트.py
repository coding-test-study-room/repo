"""
** 그리디
- 처음 잘못 생각한 부분 : 가장 무거운 두 사람이 최적의 해를 보장하지 않는다
- 수정 -> 가장 무거운 사람 + 가장 가벼운 사람
"""
from collections import deque


def solution(people, limit):
    people.sort(reverse=True)
    queue = deque(people)

    total_cnt = 0
    while queue:
        heaviest = queue.popleft()
        lightest = queue.pop() if queue else 0

        if heaviest + lightest > limit:
            queue.append(lightest)

        total_cnt += 1

    return total_cnt
