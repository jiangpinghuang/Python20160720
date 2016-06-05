# The statistics of ill-formed words in pit. #

voc = {}
oov = []
norm = []

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
def statNormWords(filePath):  
    for line in open(filePath, 'r'):
        #print line
        strs = line.split("\t")
        if strs[0].strip() not in norm:
            norm.append(strs[0].strip())
    
    normNum = 0
    totalNum = 0
    for key in voc:
        if key in norm:
            normNum += 1
            totalNum += voc[key]
    
    print "ill-formed words: ", normNum
    print "total ill-formed words: ", totalNum
    
        
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
    
    #statPITWords(train)
    #statPITWords(test)
    statPITWords(dev)    
    statOOVWords(scowl)    
    statNormWords(emnlp)
    
    #printDictWords(norm)
    index = 0
    total = 0
    for key in voc:
        #print key, voc[key]
        index += 1
        total += voc[key]
    print "index: ", index
    print "total: ", total
