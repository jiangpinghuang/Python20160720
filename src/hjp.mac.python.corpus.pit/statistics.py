# statistics the dev data.

# read file
def trainDev(path):
    C05 = 0
    C14 = 0
    C23 = 0
    C32 = 0
    C41 = 0
    C50 = 0
    for line in open(path, 'r'):
        strs = line.split('\t')
        if strs[4].strip() == '(0, 5)':
            C05 += 1
        if strs[4].strip() == '(1, 4)':
            C14 += 1
        if strs[4].strip() == '(2, 3)':
            C23 += 1
        if strs[4].strip() == '(3, 2)':
            C32 += 1
        if strs[4].strip() == '(4, 1)':
            C41 += 1
        if strs[4].strip() == '(5, 0)':
            C50 += 1

    print "C05: ", C05
    print "C14: ", C14
    print "C23: ", C23
    print "C32: ", C32
    print "C41: ", C41
    print "C50: ", C50       


if __name__ == '__main__':
    dev = '/Volumes/whu/tmp/data/pit_dev.txt'
    print dev
    trainDev(dev) 