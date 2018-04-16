import os
f = open('url.txt', 'r')
for r in f:
    r = r.strip('\n')
    os.system('git clone %s'%r)