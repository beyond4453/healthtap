import re

'''
f1 = open('10_24/heart_disease.json', 'r')
f2 = open('comp/heart_10.txt', 'w')
'''
f1 = open('11_16/heart_disease.json', 'r')
f2 = open('comp/heart_11.txt', 'w')


line1 = f1.readline()
info1 = line1.split('"')
pre_qid = info1[3]
pre_vote = info1[-2]
f2.write(pre_qid+','+pre_vote)
#line = f1.readline()

#while line :
for line in f1:
    info = line.split('"')
    cur_qid = info[3]
    print cur_qid
    cur_vote = info[-2]
    if cur_qid == pre_qid :
        f2.write(','+cur_vote)
    else :
        f2.write('\n'+cur_qid+','+cur_vote)
    pre_qid = cur_qid
    
#f2.flush()
f1.close()
f2.close()





