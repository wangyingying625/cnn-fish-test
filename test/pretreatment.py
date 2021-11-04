def loadFile(p,wFile):
    f = open(p)
    newFile=[]
    for line in f.readlines():
        newLine = line.split(',')
        newFile.append(newLine[3])
    fp = open(wFile, 'w+')
    for lines in newFile:
        fp.write(lines)
    fp.close()
    f.close()


if __name__ == '__main__':
    loadFile('./loadFile.txt','./realFile.txt')