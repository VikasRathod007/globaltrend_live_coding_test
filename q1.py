def lcs(str1, str2):
    s1len = len(str1)
    s2len = len(str2)

    if s1len == 0 or s2len == 0:
        return 0

    matrix = [["" for _ in range(s2len + 1)] for _ in range(s1len + 1)]

    for i in range(1, s1len + 1):
        for j in range(1, s2len + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + str1[i - 1]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1], key=len)

    lcs_str = matrix[-1][-1]
    return len(lcs_str)


str1 = "abcde"
str2 = "ace"
print(lcs(str1, str2))
