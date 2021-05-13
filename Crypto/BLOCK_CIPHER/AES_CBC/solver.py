#!/usr/bin/env python3
from pwn import *
from os import urandom
from binascii import hexlify, unhexlify
from Crypto.Util.number import long_to_bytes as ltb
from Crypto.Util.number import bytes_to_long as btl

host, port = 'chal.duc.tf', 30202

r = remote(host, port)

log.info('MSG "cashcashcashcash"')
know = str(r.readline().strip()).split(' ')[-1].replace("!'", "")
log.info(f'ENC MSG {know}')
iv = unhexlify(know)[16:]
log.info(f'IV {iv.hex()}')


# Intercept
plain = 'cashcashcashcash'
find = 'flagflagflagflag'
enc = unhexlify(know)[:16]

get = xor(plain, iv)
iV = xor(get, find).hex()
log.info(f'iV {iV}')

# Send message
log.info(f'INPUT {find}')
r.sendlineafter('message: ',find)

# Send  signature
sig = enc.hex() + iV

log.info(f'SIG {sig}')
r.sendlineafter('(in hex): ', sig)

r.interactive()
