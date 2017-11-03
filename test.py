import SHA_2
import hashlib
import string
import time
import itertools

start_time = time.time()


'''
Tests
'''
# SHA_2.SHA256(b'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# hash_frase = hashlib.sha256(b'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# print("Python:\t" + hash_frase.hexdigest() + "\n")
#
# SHA_2.SHA256(b'Hola')
# hash_frase = hashlib.sha256(b'Hola')
# print("Python:\t" + hash_frase.hexdigest() + "\n")
#
# SHA_2.SHA256(b'aaaa')
# hash_frase = hashlib.sha256(b'aaaa')
# print("Python:\t" + hash_frase.hexdigest() + "\n")



'''
Bruteforce a password with lowercase only
'''
#Dictionary of words, lower case only
lower = list(string.ascii_lowercase)

found = False

#Counter for length of words in dictionary
count = 0

#Amount of tries to crack the password
tries = 0

#Simulation
while not found:
    count = count + 1
    words = [''.join(i) for i in itertools.product(lower, repeat = count)]
    for each in words:
        tries = tries + 1
        #print("Try #" + str(tries) + " Elapsed time: %.1s seconds" % (time.time() - start_time))
        try_this = SHA_2.SHA256(bytes(each, 'utf-8'))
        #Password to find in SHA_2
        if try_this == SHA_2.SHA256(b'yee'):
            found = True
            print("Password: " + each + "\n" + "Tries: " + str(tries) + "\n" + "Time Elapsed: " + (time.time() - start_time))
            break
