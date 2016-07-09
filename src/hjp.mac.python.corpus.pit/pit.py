# process pit for treeLSTM.

import random
import math

# read train and valid file
def trainDev(path, wpath, flag):
    index = 0
    f = open(wpath, 'w')
    f.write("pair_ID    sentence_A    sentence_B    relatedness_score    paraphrase_judgment\n")
    for line in open(path, 'r'):
        index += 1
        sents = ""
        print line
        strs = line.split('\t')
        for i in range(len(strs)):
            print strs[i]
        if strs[4].strip() == '(0, 5)':
            print '0.0000'
            print 'non-paraphrases'
            if flag:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str("0.0") + "\t" + "0"
            else:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(0, 0.1), 2)) + "\t" + "0"
        if strs[4].strip() == '(1, 4)':
            print '0.2000'
            print 'non-paraphrases'
            if flag:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str("0.2") + "\t" + "0"
            else:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(0.1, 0.3), 2)) + "\t" + "0"
        if strs[4].strip() == '(2, 3)':
            print '0.4000'
            print 'debatable'
            if flag:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str("0.4") + "\t" + "2"
            else:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(0.3, 0.5), 2)) + "\t" + "2"
        if strs[4].strip() == '(3, 2)':
            print '0.6000'  
            print 'paraphrases'
            if flag:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str("0.6") + "\t" + "1"
            else:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(0.5, 0.7), 2)) + "\t" + "1"
        if strs[4].strip() == '(4, 1)':
            print '0.8000'  
            print 'paraphrases'
            if flag:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str("0.8") + "\t" + "1"
            else:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(0.7, 0.9), 2)) + "\t" + "1"
        if strs[4].strip() == '(5, 0)':
            print '1.0000' 
            print 'paraphrases'
            if flag:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str("1.0") + "\t" + "1"
            else:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(0.9, 1.0), 2)) + "\t" + "1" 
        print sents
        f.write(sents + '\n')
    f.close()        

# read test file  
def testData(path, wlabel, wpath, flag):
    index = 0
    f = open(wpath, 'w')
    f.write("pair_ID    sentence_A    sentence_B    relatedness_score    paraphrase_judgment\n")
    sent = []
    label = []
    for line in open(path, 'r'):        
        print line
        strs = line.split('\t')
        print(len(strs))
        print(index)
        sent.append(strs[2] + "\t" + strs[3])
    
    print wlabel
    for lines in open(wlabel, 'r'):        
        print lines
        strs = lines.split('\t')
        
        if strs[1].strip() == '0.0000':
            print '0.0000'
            print 'non-paraphrases'
            if flag:
                label.append(str("0.0") + "\t" + "0")
            else:
                label.append(str(round(random.uniform(0, 0.1), 2)) + "\t" + "0")
        if strs[1].strip() == '0.2000':
            print '0.2000'
            print 'non-paraphrases'
            if flag:
                label.append(str("0.2") + "\t" + "0")
            else:
                label.append(str(round(random.uniform(0.1, 0.3), 2)) + "\t" + "0")
        if strs[1].strip() == '0.4000':
            print '0.4000'
            print 'non-paraphrases'
            if flag:
                label.append(str("0.4") + "\t" + "0")
            else:
                label.append(str(round(random.uniform(0.3, 0.5), 2)) + "\t" + "0")          
        if strs[1].strip() == '0.6000':
            print '0.6000'  
            print 'debatable'
            if flag:
                label.append(str("0.6") + "\t" + "2")
            else:       
                label.append(str(round(random.uniform(0.5, 0.7), 2)) + "\t" + "2")           
        if strs[1].strip() == '0.8000':
            print '0.8000'  
            print 'paraphrases'
            if flag:
                label.append(str("0.8") + "\t" + "1") 
            else:
                label.append(str(round(random.uniform(0.7, 0.9), 2)) + "\t" + "1")            
        if strs[1].strip() == '1.0000':
            print '1.0000' 
            print 'paraphrases'
            if flag:
                label.append(str("1.0") + "\t" + "1") 
            else:
                label.append(str(round(random.uniform(0.9, 1.0), 2)) + "\t" + "1")            
        index += 1
    for i in range(index):
        f.write(str(i+1) + "\t" + sent[i] + "\t" + label[i] + "\n")
    f.close()

# print sentence length
def sentLength(path):
    for line in open(path, 'r'):
        strs = line.split("\t")
        str1 = strs[2].split(" ")
        str2 = strs[3].split(" ")
        step = abs(len(str1) - len(str2))
        if step > 10:
            #print line
            print 'sent1: ', strs[2]
            print 'sent2: ', strs[3]
            print line

# split line into sentences
def sentSplit(filepath, dist):
    with open(filepath) as datafile, \
         open(dist + 'id.txt', 'w') as idfile, \
         open(dist + 'ls.txt', 'w') as lsfile, \
         open(dist + 'rs.txt', 'w') as rsfile, \
         open(dist + 'sim.txt', 'w') as simfile, \
         open(dist + 'pi.txt', 'w') as pifile:
            datafile.readline()
            for line in datafile:
                print line
                id, ls, rs, sim, pi = line.strip().split('\t')
                idfile.write(id + '\n')
                lsfile.write(ls + '\n')
                rsfile.write(rs + '\n')
                simfile.write(sim + '\n')
                pifile.write(pi + '\n')

# main function   
if __name__ == '__main__':
    train = '/home/hjp/Workshop/Model/data/pit/pit_trainn.txt'
    wtrain = '/home/hjp/Workshop/Model/data/tmp/pit_train.txt'
    dev = '/home/hjp/Workshop/Model/data/pit/pit_devn.txt'
    wdev = '/home/hjp/Workshop/Model/data/tmp/pit_dev.txt'
    test = '/home/hjp/Workshop/Model/data/pit/pit_testn.txt'
    label = '/home/hjp/Workshop/Model/data/pit/pit_test_label.txt'
    wtest = '/home/hjp/Workshop/Model/data/tmp/pit_test.txt'
    strain = '/home/hjp/Workshop/Model/data/tmp/train/'
    sdev = '/home/hjp/Workshop/Model/data/tmp/dev/'
    stest = '/home/hjp/Workshop/Model/data/tmp/test/'

    trainDev(train, wtrain, True) 
    trainDev(dev, wdev, True) 
    testData(test, label, wtest, True)
    sentSplit(wtrain, strain)
    sentSplit(wdev, sdev)
    sentSplit(wtest, stest)
