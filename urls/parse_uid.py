import re

f = open('answer.json', 'r')
f2 = file('urls_uid.txt', 'w+')

'''
line = f.readline()
print line 
info = line.split('"')
print info
uid = info[11]
print uid
'''


for line in f:
    info = line.split('"')
    uid = info[11]

    f2.write("https://www.healthtap.com/experts/"+uid+"\n")
    f2.flush()
    print uid
    
f.close()
f2.close()
