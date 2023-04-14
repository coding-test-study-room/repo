"""
sol 1 -> min heap, max heap 두개의 힙큐 활용
"""
from heapq import heappush, heappop


def solution(operations):
    min_q, max_q = [], []
    size = 0  # 데이터 정합성 때문

    for operation in operations:
        op, num = operation.split()

        if op == 'I':
            num = int(num)
            heappush(min_q, num)
            heappush(max_q, (-num, num))
            size += 1
        else:  # op == 'D'
            if size == 0:  # 무시
                continue

            if num == '1':
                heappop(max_q)
            else:
                heappop(min_q)
            size -= 1

    if size == 0:
        return [0, 0]

    # 동기화 문제 -> 교집합 처리
    '''
    ex.
    input : ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]
    output : [6, 5]
    '''
    max_qs = set(map(lambda x: x[1], max_q))
    min_qs = set(min_q)
    datas = sorted(list(max_qs & min_qs))

    return [datas[-1], datas[0]]


"""
sol 2 -> 큐, 이분 탐색 활용
"""
from collections import deque
from bisect import insort_left


def solution2(operations):
    queue = deque([])

    for operation in operations:
        op, num = operation.split()

        if op == 'I':
            num = int(num)
            insort_left(queue, num)
        else:
            if not queue:
                continue

            if num == '1':
                queue.pop()
            else:
                queue.popleft()

    if not queue:
        return [0, 0]

    return [queue[-1], queue[0]]
