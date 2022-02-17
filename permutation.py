def permutation (S):
    if len(S) == 0:
        return []

    if len(S) == 1:
        return [S]

    hasil = []
    for i in range (len(S)):
        temp = S[i]
        sisa = S[:i] + S[i+1:]

        for j in permutation(sisa):
            hasil.append([temp] + j)

    return hasil