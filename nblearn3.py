import sys
import os
import glob
filename = "C:\\Users\\dnish\\Desktop\\data\\train"
count = 0
hamCount = 0
spamCount = 0
hamDict = {}
spamDict = {}
print ("name")
stopwords = ["a","an","the","in","to","from","are","as","at","be","by","for","has","he","is","it","its","of","on","was","were","will","with"]
for root, subdirs, files in os.walk(filename):
    print (root)
    if("spam" in root or "ham" in root):
        os.chdir(root)
        for file in files:
            if ".txt" not in file:
                continue
            count+=1
            #print (s)
            with open(file, "r", encoding="latin1") as name:
                for line in name:
                    line = line.lower()
                    wordlist = line.split()
                    for word in wordlist:
                        # if word == "\n" or word =="":
                        #     continue
                        if word.endswith("s"):
                            word = word[:-1]
                        elif word.endswith("ed"):
                            word = word[:-2]
                        elif word.endswith("ing"):
                            word = word[:-3]
                        if word in stopwords:
                            continue
                        if "spam" in root:
                            if(word in spamDict):
                                spamDict[word] +=1
                            else:
                                spamDict[word] = 1
                        if "ham" in root:
                            if (word in hamDict):
                                hamDict[word] += 1
                            else:
                                hamDict[word] = 1
                if "ham" in root:
                    hamCount+=1
                if "spam" in root:
                    spamCount+=1

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
    spamWord += spamDict[k]

print("spam word count"+str(spamWord))
print("ham word count"+str(hamWord))

f = open("C:\\Users\\dnish\\Desktop\\data\\nbmodel.txt", "w", encoding="latin1")
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
