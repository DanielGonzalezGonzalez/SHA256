import SHA_2
import hashlib
import string

# SHA_2.SHA256('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# hash_frase = hashlib.sha256(b'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# print("Python:\t" + hash_frase.hexdigest() + "\n")

#hash_frase = hashlib.sha256(b'Hola')
SHA_2.SHA256('Hola')
#print("Python:\t" + hash_frase.hexdigest() + "\n")

# hash_frase = hashlib.sha256(b'aaaa')
SHA_2.SHA256('aaaa')
# print("Python:\t" + hash_frase.hexdigest() + "\n")

# lower = list(string.ascii_lowercase)
#
# import itertools
# found = False
# count = 0
# tries = 0
# while not found:
#     count = count + 1
#     words = [''.join(i) for i in itertools.product(lower, repeat = count)]
#     for each in words:
#         tries = tries + 1
#         print("Try #" + str(tries))
#         try_this = SHA_2.SHA256(each)
#         if try_this == SHA_2.SHA256('ba'):
#             found = True
#             print("Password: " + each)
#             break
