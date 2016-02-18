import re

f_in1 = open('comp/heart.txt', 'r')
f_in2 = open('comp/heart_search.txt', 'r')
f_out = open('stable/heart.txt','w')

contents = f_in1.read()
print 'reading finished'

for line in f_in2:
    #print line
    info = line.split(',')
    qid = info[0]
    occur = contents.count(qid)
    print str(qid) + ' ' + str(occur)
    if occur == 1:
        f_out.write(line)

print 'program finished'    
f_in1.close()
f_in2.close()
f_out.close()


'''
def count_string_occurrence():
    string = "test"
    f = open("result_file.txt")
    contents = f.read()
    f.close()
    print "Number of '" + string + "' in file", contents.count("foo")
'''
