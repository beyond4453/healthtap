import re

f = open('question.json', 'r')
f2 = file('urls_qid.txt', 'w+')
'''
line = f.readline()
print line

#line = line.strip('\n').strip(',').strip('{').strip('}')
#print line
info = line.split('"')
print info
print info[-2]

f2.close()
f.close()

'''

for line in f:
    #line = line.strip('\n').strip(',').strip('{').strip('}')
    #print line
    info = line.split('"')
    qid = info[-2]

    # you need to flush it !!!!!!!!!!
    f2.write("https://www.healthtap.com/user_questions/"+qid+'\n')
    f2.flush()
    print qid
f2.close
f.close



