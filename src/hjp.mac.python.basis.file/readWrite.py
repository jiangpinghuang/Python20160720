file1 = "/home/hjp/Workshop/Model/w2vc/twittera.txt"
file2 = "/home/hjp/Workshop/Model/w2vc/twitterb.txt"

file = "/home/hjp/Workshop/Model/w2vc/twitter.txt"

f = open(file, 'w')

print "write file1..."
index = 0
for line in open(file1, 'r'):
    index += 1
    print line
    if index < 12345689: 
        f.write(line)

print "write file2..."
    
for line in open(file2, 'r'):
    #print line 
    f.write(line)

f.close()
