import random
import operator

def ksa(key):
    key_length = len(key)
    # membuat array "S"
    S = list(range(256))  

    random.seed(key_length % 256)
    random.shuffle(S)

    return S

def prga(S, text: bytes):
    # S array dari KSA
    # n panjang plaintext

    i = 0
    j = 0
    C = []

    arr = []
    for byte in text:
        arr.append(byte)
    
    for k in range(len(text)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        #Swap
        S[i], S[j] = S[j], S[i]

        keystream = S[(S[i] + S[j]) % 256]

        # C += str(keystream.to_bytes(1, 'big') ^ ord(text[k]).to_bytes(1, 'big'))
        C.append(keystream ^ arr[k])


    return bytearray(C)

def myowncipher(key, base):
    # print(base)
    # print(type(base))
    # key = [ord(c) for c in key]
    # base = [ord(c) for c in base]
    S = ksa(key)
    hasil = prga(S, base)
    
    return hasil

# tes = myowncipher("abcd", "lololol")

# print(myowncipher("abcd", "lololol"))
# print(myowncipher("abcd", tes))