def solution(n, arr1, arr2):
    for i in range(n):
        arr1[i] = toBinary(arr1[i], n)
        arr2[i] = toBinary(arr2[i], n)

    answer = []
    for i in range(n):
        row = ""
        for j in range(n):
            if arr1[i][j] == 0 and arr2[i][j] == 0:
                row += " "
            else:
                row += "#"
        answer.append(row)
    return answer

def toBinary(num, n):
    binary = []
    digit = [2**(n-i-1) for i in range(n)]
    for i in digit:
        binary.append(num // i)
        num %= i
    return binary

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))