import os
f = open("p4files","r")
f1 = open("p4file","w")
lines = f.readlines()
for line in lines:
    if "include" in line:
        continue
    if "compiled" in line:
	continue;
    if "head" in line:
	continue
    if "parser" in line:
  	continue
    f1.write(line)
f1.close()
f.close()

