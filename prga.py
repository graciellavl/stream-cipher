def prga(S, text):
    # S array dari KSA
    # n panjang plaintext

    i = 0
    j = 0
    C = ''
    for k in range(len(text)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        #Swap
        S[i], S[j] = S[j], S[i]

        keystream = S[(S[i] + S[j]) % 256]
        C += chr(ord(keystream) ^ ord(text[k]))

    return C

    

        