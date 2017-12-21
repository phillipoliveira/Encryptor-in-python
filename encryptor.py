import random, string
from string import printable
from itertools import cycle

def set_key():
    global public_key, private_key
    public_key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(64))
    private_key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(64))
    return public_key, private_key

def encrypt(strg):
    global public_key, private_key
    strg = filter(lambda x: x in (set(string.printable)), strg)
    k1,k2,l = cycle(iter(public_key)),cycle(iter(private_key)),[]
    for i in strg:
        val1,val2 = next(k1),next(k2)
        try: 
            crypt = ord(i) + ord(val1) - ord(val2)
            while crypt > 126:
                crypt -= 126
            while crypt < 33:
                crypt += 126
            print(crypt)
            l.append(crypt)
        except:
            continue
    return "".join(map(chr,l))

def decrypt(strg):
    global public_key, private_key
    k1,k2,l = cycle(iter(public_key)),cycle(iter(private_key)),[]
    for i in strg:
        val1,val2 = next(k1),next(k2)
        try:
            crypt = ord(i) - ord(val1) + ord(val2)
            while crypt < 33:
                crypt += 126
            while crypt > 126:
                crypt -= 126
            l.append(crypt)
        except:
            continue
    return "".join(map(chr,l))

def decrypt__secret_key(encrypted,decrypted,public_key):
        for v in decrypted:
            l = []
            char = (ord(v) 
                    + ord(next(cycle(iter(public_key))))
                    - ord(next(cycle(iter(encrypted))))
                    )
            while char < 33:
                char += 126
            while char > 126:
                char -= 126
            print(chr(char))
