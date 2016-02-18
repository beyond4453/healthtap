import re

#tempfiles = ['qapair1.txt','qapair2.txt','qapair3.txt','qapair4.txt','qapair5.txt']
tempfiles = ['allergy.txt','arthitis.txt','asthma.txt','depression.txt','heart.txt']

f = open('answer.txt', 'w')
with open('answer.txt','w') as fo:
    for tempfile in tempfiles:
        with open(tempfile,'r') as fi:
            fo.write(fi.read())

print 'finished' 
    
 
