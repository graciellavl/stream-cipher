def prga(S, n):
    # S array dari KSA
    # n panjang plaintext
    
    i = 0
    j = 0
    key = []
    while (n>0):
        n -= 1
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        #Swap
        temp = S[i]
        S[i] = S[j]
        S[j] = temp

        K = S[(S[i] + S[j]) % 256]
        key.append(K)

    return key

        