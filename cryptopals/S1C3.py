'''
The hex encoded string:
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.
You can do this by hand. But don't: write code to do it for you.
How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.
'''

import string

def scoring(s):
    sc = {}
    sc[" "] = 256
    sc["e"] = 255
    sc["t"] = 254
    sc["a"] = 253
    sc["o"] = 252
    sc["i"] = 251
    sc["n"] = 250
    sc["s"] = 249
    sc["h"] = 248
    sc["r"] = 247
    sc["d"] = 246
    sc["l"] = 245
    sc["u"] = 244
    out = 0
    try:
        test = s.lower()
    except:
        return 0
    for l in s.lower():
        if l in sc:
            out+=sc[l]
    return out


def xor(input, x):
    out = bytearray(len(input))
    for i in range(len(input)):
        out[i] = input[i] ^ x
    return out


enc = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
dec_b = bytearray.fromhex(enc)

comp = {}
for f in range(255):
    try:
        passable = all(ch in string.printable for ch in xor(dec_b, f).decode())
        comp[chr(f)] = scoring(xor(dec_b, f).decode())
    except:
        continue

comp = {k:v for k, v in comp.items() if v>0 and k in string.ascii_letters}

print(max(comp.values()))
print({k:v for k, v in comp.items() if v == max(comp.values())})
