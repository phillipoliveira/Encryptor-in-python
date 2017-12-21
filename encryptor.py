import random, string
from itertools import cycle

def set_key():
    global key
    key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(64))
    return key

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

def decrypt_key(encrypted,decrypted):
    if len(encrypted) < 64:
        print("You must use a string longer than 64 characters to decrypt the whole key.")
        return
    else:
        g,l = cycle(iter(encrypted)),[]
        for v in decrypted:
            val = next(g)
            char = ord(v) - ord(val) 
            if char > 0:
                char -= 126
            char = abs(char)
            l.append(char)
        return "".join(map(chr,l))
