import r2pipe
import os

#def doSolve(vcmp, vrand):
#    pass

r2 = r2pipe.open('./main')
r2.cmd('e dbg.profile=re2.rr2')
r2.cmd('aaa; ood; db main; db 0x08049209')
r2.cmd('dc')
print(r2.cmd('pdf'))
r2.cmd('dc')
print(r2.cmd('pdf'))
print(r2.cmd('drr'))
