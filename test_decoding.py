import random
import numpy as np
import math

ENC_s = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
        ])

basesam_pro = [0.3595, 0.3092, 0.1966, 0.0925, 0.0322, 0.0083, 0.0016,
               2.2e-04, 2.3e-05, 1.77e-06, 1.01e-07, 4.24e-9, 1.32e-10,
               3.04e-11, 5.17e-13, 6.51e-15, 6.1e-17, 4.2e-19, 2.12e-21] 


success_pro = [[0.9976, 0.9976, 0.992, 0.9956, 0.992, 0.99996],
                [0.9872, 0.996, 0.9808, 0.9964, 0.9928, 0.99993],
                [0.9504, 0.9932, 0.9408, 0.9884, 0.9904, 0.99991],
                [0.8976, 0.9708, 0.898, 0.9824, 0.9904, 0.996]]

## dnn chanel 
def BSC_channel(input_bits, itr):
    err = [0] * len(input_bits)
    for i in range(6):
        if random.random() > success_pro[itr][i]:
            err[i] = 1
    for i in range(6, len(input_bits)):
        if random.random() > success_pro[itr][5]:
            err[i] = 1
    out_bits = np.bitwise_xor(input_bits, err)
    return out_bits

        ##decoding scheme
def decoding_scheme(noz_bits, itr):
    pro_code = [0] * 19
    corrected_bits = 0
    best_pro = -10000
    best_pick = 0
    for j in range(19):
        hamming_code = np.bitwise_xor(ENC_s[j,:], noz_bits)
        pro_code[j] = math.log10(basesam_pro[j])
        for i in range(len(hamming_code)):
            if i < 6:
                p = success_pro[itr][i]
                pro_code[j] += (math.log10(1 - p) - math.log10(p))*hamming_code[i] + math.log10(p)
            else:
                p = success_pro[itr][5]
                pro_code[j] += (math.log10(1 - p) - math.log10(p))*hamming_code[i] + math.log10(p)
        if pro_code[j] > best_pro:
            best_pick = j
            best_pro = pro_code[j]

    corrected_bits = ENC_s[best_pick, :]

    return corrected_bits


c = [0] * 18
itr = 3
t = BSC_channel(c, itr)
print(t)
corret_t = decoding_scheme(t, itr)
print(corret_t)