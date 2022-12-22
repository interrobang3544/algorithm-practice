def solution(strings, n):
    answer = sorted(sorted(strings), key = lambda a: a[n])
    return answer

print(solution(["abce", "abcd", "cdx"],	2))