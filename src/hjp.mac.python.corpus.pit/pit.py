# process pit for treeLSTM.

import random

# read file
def trainDev(path, wpath):
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
            sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(0, 0.5), 1)) + "\t" + "non-paraphrases"
        if strs[4].strip() == '(1, 4)':
            print '0.2000'
            print 'non-paraphrases'
            sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(0.5, 1.5), 1)) + "\t" + "non-paraphrases"
        if strs[4].strip() == '(2, 3)':
            print '0.4000'
            print 'debatable'
            sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(1.5, 2.5), 1)) + "\t" + "debatable"
        if strs[4].strip() == '(3, 2)':
            print '0.6000'  
            print 'paraphrases'
            sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(2.5, 3.5), 1)) + "\t" + "paraphrases"
        if strs[4].strip() == '(4, 1)':
            print '0.8000'  
            print 'paraphrases'
            sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(03.5, 4.5), 1)) + "\t" + "paraphrases"
        if strs[4].strip() == '(5, 0)':
            print '1.0000' 
            print 'paraphrases'  
            sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(4.5, 5.0), 1)) + "\t" + "paraphrases" 
        print sents
        f.write(sents + '\n')
    f.close()
        
  
def testData(path, wlabel, wpath):
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
            label.append(str(round(random.uniform(0, 0.5), 1)) + "\t" + "non-paraphrases")
        if strs[1].strip() == '0.2000':
            print '0.2000'
            print 'non-paraphrases'
            label.append(str(round(random.uniform(0.5, 1.5), 1)) + "\t" + "non-paraphrases")
        if strs[1].strip() == '0.4000':
            print '0.4000'
            print 'non-paraphrases'
            label.append(str(round(random.uniform(1.5, 2.5), 1)) + "\t" + "non-paraphrases")          
        if strs[1].strip() == '0.6000':
            print '0.6000'  
            print 'debatable'
            label.append(str(round(random.uniform(2.5, 3.5), 1)) + "\t" + "debatable")           
        if strs[1].strip() == '0.8000':
            print '0.8000'  
            print 'paraphrases'
            label.append(str(round(random.uniform(3.5, 4.5), 1)) + "\t" + "paraphrases")            
        if strs[1].strip() == '1.0000':
            print '1.0000' 
            print 'paraphrases'  
            label.append(str(round(random.uniform(4.5, 5.0), 1)) + "\t" + "paraphrases")            
        index += 1
    for i in range(index):
        f.write(str(i+1) + "\t" + sent[i] + "\t" + label[i] + "\n")
    f.close()


if __name__ == '__main__':
    train = '/home/hjp/Workshop/Model/data/pit/pit_train.txt'
    wtrain = '/home/hjp/Workshop/Model/data/tmp/pit_train.txt'
    dev = '/home/hjp/Workshop/Model/data/pit/pit_dev.txt'
    wdev = '/home/hjp/Workshop/Model/data/tmp/pit_dev.txt'
    test = '/home/hjp/Workshop/Model/data/pit/pit_test.txt'
    label = '/home/hjp/Workshop/Model/data/pit/pit_test_label.txt'
    wtest = '/home/hjp/Workshop/Model/data/tmp/pit_test.txt'

    trainDev(train, wtrain) 
    trainDev(dev, wdev) 
    testData(test, label, wtest)
    