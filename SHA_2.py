import sys
import binascii
def SHA256(frase):

    ror = lambda val, r_bits, max_bits: \
        ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
        (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
       0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
       0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
       0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
       0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
       0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
       0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
       0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

    #print("%x" % ror(k[0], 8, 32))

    original_message = frase
    size_of_message = sys.getsizeof(original_message)
    altered_message = original_message + "1"

    K = 0
    while (K + 1 + size_of_message + 64) % 512 != 0:
        altered_message = altered_message + "0"
        K = K + 1

    extra = str(size_of_message.to_bytes(16, byteorder='big'))
    extra = extra[2:len(extra)-1]

    altered_message = altered_message + extra
    altered_message = bytes(altered_message, 'utf-8')
    #print(altered_message)
    message_chunks = [altered_message[i:i+512] for i in range(0, len(altered_message), 513)]
    #print(message_chunks)
    for chunk in message_chunks:
        #new_chunk = "".join("{:01x}".format(ord(c)) for c in chunk)

        w = [0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
            0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
            0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
            0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
            0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
            0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
            0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
            0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,]

        for i in range(0, 16, 1):
            w[i] = int(binascii.hexlify(chunk[i:i+32]), 16)
            #w[i] = int(binascii.hexlify(chunk), 16)
            #print(w[i])

        for i in range(16, 64, 1):
            #print(w[i-15], ror(w[i-15], 7, 32))
            s0 = ror(w[i-15], 8, 32) ^ ror(w[i-15], 19, 32) ^ (w[i-15] >> 3)
            s1 = ror(w[i-2], 18, 32) ^ ror(w[i-2], 20, 32) ^ (w[i-2] >> 10)
            w[i] = (((((w[i-16] + s0) % (1 << 32)) + w[i-7]) % (1 << 32)) + s1) % (1 << 32)
            w[i] = (w[i-16] + s0 + w[i-7] + s1) % (1 << 32)
            #print(w[i])


        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7

        for i in range(0, 64, 1):
            S1 = ror(e, 7, 32) ^ ror(e, 12, 32) ^ ror(e, 26, 32)
            ch = (e & f) ^ ((~e) & g)
            temp1 = (((((((h + S1) % (1 << 32)) + ch) % (1 << 32)) + k[i]) % (1 << 32)) + w[i]) % (1 << 32)
            S0 = ror(a, 3, 32) ^ ror(a, 14, 32) ^ ror(a, 23, 32)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) % (1 << 32)

            h = g
            g = f
            f = e
            e = (d + temp1) % (1 << 32)
            d = c
            c = b
            b = a
            a = (temp1 + temp2) % (1 << 32)

        h0 = (h0 + a) % (1 << 32)
        h1 = (h1 + b) % (1 << 32)
        h2 = (h2 + c) % (1 << 32)
        h3 = (h3 + d) % (1 << 32)
        h4 = (h4 + e) % (1 << 32)
        h5 = (h5 + f) % (1 << 32)
        h6 = (h6 + g) % (1 << 32)
        h7 = (h7 + h) % (1 << 32)

    digest = ("%0.2x" % h0) + ("%0.2x" % h1) + ("%0.2x" % h2) + ("%0.2x" % h3) + ("%0.2x" % h4) + ("%0.2x" % h5) +("%0.2x" % h6) + ("%0.2x" % h7)
    print("Frase:\t" + frase + "\n" + "Mia:\t" + digest)
    return digest