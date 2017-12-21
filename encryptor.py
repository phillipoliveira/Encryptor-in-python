import string
import random
from itertools import cycle

def set_key():
    global key
    key = "".join(random.sample((set(string.printable)),64))

def encrypt(strg):
    global key
    strg = filter(lambda x: x in (set(string.printable)), strg)
    g,l = cycle(iter(key)),[]
    for i in strg:
        val = next(g)
        try:
            crypt = ord(i) + ord(val)
            if crypt > 126:
                crypt -= 126
            l.append(crypt)
        except:
            continue
    return "".join(map(chr,l))

def decrypt(string):
    global key
    g,l = cycle(iter(key)),[]
    for i in string:
        val = next(g)
        try:
            crypt = ord(i) - ord(val)
            if crypt < 0:
                crypt += 126
            l.append(crypt)
        except:
            continue
    return "".join(map(chr,l))
