import re

f1 = open('comp/heart_10.txt', 'r')
f2 = open('comp/heart_11.txt', 'r')
f_out1 = open('comp/heart.txt', 'w+')

t = set()

for line in f1:
    print line
    t.add(line)
for line in f2:
    print line
    t.add(line)
for e in t:
    f_out1.write(e)
    print e



f1.close()
f2.close()
f_out1.close()
