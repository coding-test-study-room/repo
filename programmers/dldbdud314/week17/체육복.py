"""
** greedy -> set 활용
"""


def solution(n, lost, reserve):
    r_set = set(reserve) - set(lost)
    l_set = set(lost) - set(reserve)

    cnt = 0
    for x in sorted(l_set):
        if x - 1 in r_set:
            r_set.remove(x - 1)
        elif x + 1 in r_set:
            r_set.remove(x + 1)
        else:
            cnt += 1  # 빌릴 수 없음

    return n - cnt
