import SHA_2
import hashlib
import string
import time

start_time = time.time()

# SHA_2.SHA256(b'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# hash_frase = hashlib.sha256(b'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# print("Python:\t" + hash_frase.hexdigest() + "\n")
#
# hash_frase = hashlib.sha256(b'Hola')
# SHA_2.SHA256(b'Hola')
# print("Python:\t" + hash_frase.hexdigest() + "\n")
#
# hash_frase = hashlib.sha256(b'aaaa')
# SHA_2.SHA256(b'aaaa')
# print("Python:\t" + hash_frase.hexdigest() + "\n")

lower = list(string.ascii_lowercase)

import itertools
found = False
count = 0
tries = 0
while not found:
    count = count + 1
    words = [''.join(i) for i in itertools.product(lower, repeat = count)]
    for each in words:
        tries = tries + 1
        #print("Try #" + str(tries) + " Elapsed time: %.1s seconds" % (time.time() - start_time))
        try_this = SHA_2.SHA256(bytes(each, 'utf-8'))
        if try_this == SHA_2.SHA256(b'yee'):
            found = True
            print("Password: " + each + "\n" + "Tries: " + str(tries) + "\n" + "Time Elapsed: " + (time.time() - start_time))
            break
