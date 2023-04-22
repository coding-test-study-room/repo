from heapq import heappush, heappop


def solution(scoville, K):
    # min heap 만들기
    queue = []
    for x in scoville:
        heappush(queue, x)

    # 조건 만족할 때까지 섞기
    cnt = 0
    while queue:
        # 가장 맵지 않은 스코빌 지수가 K 이상이면 끚.
        if queue[0] >= K:
            return cnt

        if len(queue) == 1:
            break

        heappush(queue, heappop(queue) + heappop(queue) * 2)
        cnt += 1

    return -1
