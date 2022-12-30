def find_max(a, n):
    r = len(a)-1
    if r == n-1:
        return 1
    ans = 0
    for c in range(n):
        go = True
        p = 0
        while p < len(a) and go:
            j = 0
            if c == a[p]:
                go = False
                break
            for j in range(n):
                if (r+1 == p+j and c == a[p]+j) or (r+1 == p+j and c == a[p]-j) or (r+1 == p-j and c == a[p]+j) or (r+1 == p-j and c == a[p]-j):
                    go = False
                    break
            p += 1
        if go:
            ans += find_max(a+[c], n)
    return ans


def solution(n):
    return find_max([], n)