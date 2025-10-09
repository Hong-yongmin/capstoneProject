import time
from Crypto.Util.number import getPrime

key_size = int(input("key size:"))
prime_size = key_size // 2

p = getPrime(prime_size)
q = getPrime(prime_size)
n = p * q

start = time.time()
for i in range(3, n):
    if n % i == 0:
        end = time.time()
        print("p = {0}, q = {1}".format(i, n//i))
        print("time = {0}".format(end-start))
        break