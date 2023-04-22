"""
** Kruskal 알고리즘
"""


def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]


def union_parent(p, n1, n2):
    if n1 < n2:
        p[n2] = n1
    else:
        p[n1] = n2


def solution(n, costs):
    # 부모 테이블 자기자신으로 초기화
    parent = [i for i in range(n)]

    # 간선 정보 -> 오름차순 정렬
    edges = []
    for a, b, c in costs:
        edges.append((c, a, b))
    edges.sort()

    # kruskal 수행
    total_cost = 0
    for c, a, b in edges:
        p1 = find_parent(parent, a)
        p2 = find_parent(parent, b)

        if p1 != p2:
            union_parent(parent, p1, p2)
            total_cost += c

    return total_cost
