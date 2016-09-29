import sys
import os
import glob

filename = "C:\\Users\\dnish\\Desktop\\data\\train"
count = 0
hamCount = 0
spamCount = 0
hamDict = {}
spamDict = {}
isSpam = False
isHam = False
currDir = os.getcwd()
for root, subdirs, files in os.walk(filename):
    print (root)
    isSpam = os.path.basename(os.path.normpath(root)) == "spam"
    isHam = os.path.basename(os.path.normpath(root)) == "ham"
    if( isSpam or isHam):
        os.chdir(root)
        for file in files:
            if ".txt" not in file:
                continue
            count+=1
            #print (s)
            with open(file, "r", encoding="latin1") as name:
                for line in name:
                    wordlist = line.split()
                    for word in wordlist:
                        # if word == "\n" or word =="":
                        #     continue
                        if isSpam:
                            if(word in spamDict):
                                spamDict[word] +=1
                            else:
                                spamDict[word] = 1
                        if isHam:
                            if (word in hamDict):
                                hamDict[word] += 1
                            else:
                                hamDict[word] = 1
                if isHam:
                    hamCount+=1
                if isSpam:
                    spamCount+=1
                # print(file)

for key in hamDict:
    if key not in spamDict:
        spamDict[key] = 0
    hamDict[key] +=1

for key in spamDict:
    if key not in hamDict:
        hamDict[key] = 1
    spamDict[key] += 1


spamWord = 0
hamWord = 0

for k in hamDict:
    hamWord +=hamDict[k]
for k in spamDict:
    spamWord += spamDict[k]

print("spam word count"+str(spamWord))
print("ham word count"+str(hamWord))
os.chdir(currDir)
f = open("nbmodel.txt", "w", encoding="latin1")
f.write(str(spamCount/count)+" \n")
f.write(str(hamCount/count)+" \n")
for k in hamDict:
    val = hamDict[k]/hamWord
    f.write(k+" "+str(val)+" \n")
f.write("Spam Prob \n")
for k in spamDict:
    val = spamDict[k]/spamWord
    f.write(k+" "+str(val)+" \n")
f.flush()
f.close()
