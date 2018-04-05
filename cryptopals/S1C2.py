'''
Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.
If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965
... should produce:
746865206b696420646f6e277420706c6179
'''

import codecs

def xor(input,x):
    out = bytearray(len(input))
    for i in range(len(input)):
        out[i] = input[i]^x[i]
    return codecs.encode(bytes(out),"hex")

s = bytearray.fromhex("1c0111001f010100061a024b53535009181c")
h = bytearray.fromhex("686974207468652062756c6c277320657965")
print(xor(s,h))
