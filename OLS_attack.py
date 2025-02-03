import falcon
from samplerz import samplerz
import numpy as np

def l1_distance(a, b):
    c = np.array(b)
    return np.sum(np.abs(a - c))

N = 512 # falcon secret polynomial dimension, you can choose 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024
sam_num = 40000 # number of samples (s,z)

sk = falcon.SecretKey(N)
f = sk.f
g = sk.g
f_inv = [-x for x in f]
b_real = g + f_inv

print("Collecting the samples (s,z)")

b_est, t_est= sk.OLSattack(sam_num) #b_est: estimation of b_real, t_est: time for computing b_est
b = list(map(int,np.round(b_est)))

print("First row of secret basis B: ", b_real)

if b == b_real:
    print("Successfully find the first row of secret basis B")
else:
    a = np.array(b_real)
    print("The estimation of first row: ", b)
    dist = l1_distance(a,b)
    print(f"The L1 norm difference between the first and second rows is {dist}.")

print("It take ",t_est,"sec for estimating B^{-1} using", sam_num, "samples")

