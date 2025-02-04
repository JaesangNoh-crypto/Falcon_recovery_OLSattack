# In this code, the MAP decoding algorithm is implemented to correct errors when z0 is estimated using a binary classifier for z+ in {0,1}
from samplerz import basesampler
import numpy as np
import math
import random
from os import urandom
from tqdm import tqdm


sam_num = 100000 # simulation number of samples
success_pro = [0.9976, 0.9976, 0.992, 0.9956, 0.992, 0.99996]
# Success rate of the binary classifier (MLP). This is the example!


z0s = [] # BaseSampler outputs
estz0s = [] # Estimation of BaseSampler outputs

basesam_pro = [0.3595, 0.3092, 0.1966, 0.0925, 0.0322, 0.0083, 0.0016,
        2.2e-04, 2.3e-05, 1.77e-06, 1.01e-07, 4.24e-9, 1.32e-10,
        3.04e-11, 5.17e-13, 6.51e-15, 6.1e-17, 4.2e-19, 2.12e-21]
# The probability for generating z_0 in {0,1,2,...,18} from the BaseSampler


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

def Integer_to_Binary(z0):
    z = np.abs(z0)
    z_binary = np.zeros(18, dtype = int)
    for i in range(z):
        z_binary[i] = 1
    return z_binary


# Simulation channel of the binary classifier
def BSC_channel(input_bits):
    err = [0] * len(input_bits)
    for i in range(6):
        if random.random() > success_pro[i]:
            err[i] = 1
    for i in range(6, len(input_bits)):
        if random.random() > success_pro[5]:
            err[i] = 1
    out_bits = np.bitwise_xor(input_bits, err)
    return out_bits

## MAP decoding scheme
def decoding_scheme(noz_bits):
    pro_code = [0] * 19
    corrected_bits = 0
    best_pro = -10000
    best_pick = 0
    for j in range(19):
        hamming_code = np.bitwise_xor(ENC_s[j,:], noz_bits)
        pro_code[j] = math.log10(basesam_pro[j])
        for i in range(len(hamming_code)):
            if i < 6:
                p = success_pro[i]
                pro_code[j] += (math.log10(1 - p) - math.log10(p))*hamming_code[i] + math.log10(p)
            else:
                p = success_pro[5]
                pro_code[j] += (math.log10(1 - p) - math.log10(p))*hamming_code[i] + math.log10(p)
        if pro_code[j] > best_pro:
            best_pick = j
            best_pro = pro_code[j]

    corrected_bits = ENC_s[best_pick, :]

    return corrected_bits

def Binary_to_Integer(bits):
    z0 = np.sum(bits)
    return z0 

# Generation of true z0!
print("Generating z0 using BaseSampler")
for _ in tqdm(list(range(sam_num))):
    z0 = basesampler(randombytes=urandom)
    z0s.append(z0)

decoding_num  = 0

print("Executing the MAP decoding")
# Let estimate z0!
for i in tqdm(list(range(sam_num))):
    z_true = z0s[i]
    bits = Integer_to_Binary(z_true)
    noiz_bits = BSC_channel(bits)
    dec_bits = decoding_scheme(noiz_bits)
    estz0s.append( Binary_to_Integer(dec_bits))  
    decoding_num = decoding_num + 1

print("Success rate of MAP decoding:", decoding_num/sam_num*100, "%")
