import re

f1 = open('answer.json', 'r')
f2 = open('vote.txt', 'w+')

'''
line = f1.readline()
#print line
info = line.split('"')
print info 
print info[3]
print info[7]
print info[-2]
'''

for line in f1:
    info = line.split('"')
    qid = info[3]
    aid = info[7]
    vote = info[-2]
    print qid
    
    f2.write("qid: "+qid+" aid: "+aid+" vote: "+vote+'\n')
    f2.flush()

f1.close()
f2.close()
