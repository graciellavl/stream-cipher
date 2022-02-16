def ksa(key):
    key_length = len(key)
    # membuat array "S"
    S = list(range(256))  
    x = 0
    for i in range(256):
        x = (x + S[i] + key[i % key_length]) % 256
        S[i], S[x] = S[x], S[i]  # menukar posisi objek ke i dan ke x pada array S

    return S