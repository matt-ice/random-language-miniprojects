'''
One of the 60-character strings in this file has been encrypted by single-character XOR.
Find it.
(Your code from #3 should help.)
'''

import string
import urllib.request

lines = urllib.request.urlopen(r"https://cryptopals.com/static/challenge-data/4.txt").read().splitlines()
best_guesses = {}

def scoring(s):
    sc = {}
    sc[' '] = 700000000
    sc['e'] = 390395169
    sc['t'] = 282039486
    sc['a'] = 248362256
    sc['o'] = 235661502
    sc['i'] = 214822972
    sc['n'] = 214319386
    sc['s'] = 196844692
    sc['h'] = 193607737
    sc['r'] = 184990759
    sc['d'] = 134044565
    sc['l'] = 125951672
    sc['u'] = 88219598
    sc['c'] = 79962026
    sc['m'] = 79502870
    sc['f'] = 72967175
    sc['w'] = 69069021
    sc['g'] = 61549736
    sc['y'] = 59010696
    sc['p'] = 55746578
    sc['b'] = 47673928
    sc['v'] = 30476191
    sc['k'] = 22969448
    sc['x'] = 5574077
    sc['j'] = 4507165
    sc['q'] = 3649838
    sc['z'] = 2456495
    out = 0
    try:
        test = s.lower()
    except:
        return 0
    for q in s.lower():
        if q in sc:
            out += sc[q]
    return out


def xor(inp, x):
    out = bytearray(len(inp))
    for i in range(len(inp)):
        out[i] = inp[i] ^ x
    return out


def results(l):
    comp = {}
    for f in range(255):
        try:
            passable = all(ch in string.printable for ch in xor(l, f).decode())
            comp[chr(f)] = scoring(xor(l, f).decode())
        except:
            continue
    comp = {k:v for k, v in comp.items() if v>0 and k in string.ascii_letters}
    best = {k for k, v in comp.items() if v == max(comp.values())}
    b2 = ''.join(str(a) for a in list(best))
    if b2 in best_guesses:
        best_guesses[b2] += 1
    else:
        best_guesses[b2] = 1

for l in lines:
    if l[-1]=="\n":
        results(l[:-1])
    else:
        results(l)

res = ''.join(str(k) for k in {k for k,v in best_guesses.items() if v == max(best_guesses.values())})
print(best_guesses)

for l in lines:
    print(xor(l,ord(res)).decode())



