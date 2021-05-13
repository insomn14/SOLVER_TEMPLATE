#!/usr/bin/python3

import os
import re
import r2pipe

'''
Cheatsheet :
	- dr eax=0x1337 # edit value of register eax
	- af ([name]) ([addr])  # analyze functions (start at addr or $$) or define function
	- pdi @ ([addr]) # like 'pi', with offset and bytes or print disassembly instruction from current address
	- px ([len]) ([addr/regs]) # show hexdump of address/register
'''


conti = lambda r2, num=1: r2.cmd('dc; '*num)
stepi = lambda r2, num=1: r2.cmd(f'ds {num}')
overwrite = lambda value, address: r2.cmd(f'wx {value.hex()} @ {address}')

def context(func=''):
	register = r2.cmd(f'pdf {func}')
	disassembly = r2.cmd('drr')  
	print(disassembly)
	print(register)


def startDebug(r2, args):
	r2.cmd(f'aaa; ood {args}')
	func = r2.cmd('afl')

	# Get address
	main = int(re.findall(r'(0x\w+) .*main', func)[0],16)

	# Set breakpoints



if __name__ == '__main__':
	binary = ''
	args = ''

	r2 = r2pipe.open(binary)
	startDebug(r2, args)


