# The statistics of ill-formed words in pit. #

voc = {}
oov = []
norm = {}

def statPITWords(filePath):
    for line in open(filePath, 'r'):
        strs = line.split('\t')
        str1 = strs[2].split(' ')
        for i in range(len(str1)):
            if str1[i] not in voc:
                voc[str1[i]] = 1
            else:
                voc[str1[i]] += 1
            #if str1[i] is "u":
            #    print str1    
        str2 = strs[3].split(' ')
        for j in range(len(str2)):
            if str2[j] not in voc:
                voc[str2[j]] = 1
            else:
                voc[str2[j]] += 1
            #if str2[j] is "u":
            #    print str2    


# Import oov words into oov array.
def statOOVWords(filePath):  
    for line in open(filePath, 'r'):
        #print line
        if line.strip() not in oov:
            oov.append(line.strip())
    
    wordNum = 0
    
    for key in voc:
        if key in oov:
            wordNum += 1
            
    print "wordNum: ", wordNum
    #print "oov: ", (len(voc) - wordNum)
       

# Import oov words into oov array.            
def statNormWords(pit, emnlp, wtrain): 
    f = open(wtrain, 'w') 
    for line in open(emnlp, 'r'):
        #print line
        strs = line.split("\t")
        if strs[0].strip() not in norm:
            norm[strs[0].strip()] = strs[1].strip()

    for line in open(pit, 'r'):
        strs = line.split("\t")
        str1 = strs[2]
        str1s = str1.split(" ")
        for i in range(len(str1s)):
            if str1s[i].strip() in norm:
                str1s[i] = norm[str1s[i]]
        str2s = strs[3].split(" ")
        for j in range(len(str2s)):
            if str2s[j].strip() in norm:
                print 'str2s[j]1: ', str2s[j]
                str2s[j] = norm[str2s[j]]
                print 'str2s[j]2: ', str2s[j]
        stra = ""
        for i in range(len(str1s)):
            if i == 0:
                stra = str1s[0]
            else:
                stra = stra + " " + str1s[i]
        #print "before: ", strs[2]
        #print "after: ", str
        strb = ""
        for i in range(len(str2s)):
            if i == 0:
                strb = str2s[0]
            else:
                strb = strb + " " + str2s[i]
        print "before: ", strs[3]
        print "after: ", strb
        sent = strs[0] + "\t" + strs[1] + "\t" + stra + "\t" + strb + "\t" + strs[4] + "\t" + strs[5]
        print "line: ", line
        print "sent: ", sent
        f.write(sent)
    f.close()
        
def printDictWords(dict):
    print len(dict)
    #tmp = sorted(dict)
    #for i in range(len(tmp)):
    #    print i, tmp[i]  
        
    
if __name__ == '__main__':
    train = '/Volumes/whu/tmp/data/pit_train.txt'
    test = '/Volumes/whu/tmp/data/pit_test.txt'
    dev = '/Volumes/whu/tmp/data/pit_dev.txt'    
    scowl = '/Volumes/whu/tmp/data/scowl.txt'
    emnlp = '/Volumes/whu/tmp/data/emnlp.txt'
    wtrain = '/Volumes/whu/tmp/data/pit_test1.txt'
    
    #statPITWords(train)
    #statPITWords(test)
#     statPITWords(dev)    
#     statOOVWords(scowl)    
    statNormWords(test, emnlp, wtrain)
    
    #printDictWords(norm)
#     index = 0
#     total = 0
#     for key in voc:
#         #print key, voc[key]
#         index += 1
#         total += voc[key]
#     print "index: ", index
#     print "total: ", total
