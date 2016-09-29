import sys
import os 
import glob
import math

hamDict = {}
spamDict = {}
sBool = False
hamP = 0
spamP = 0
count = 0
filename = "C:\\Users\\dnish\\Desktop\\data\\dev"
name = open("C:\\Users\\dnish\\Desktop\\data\\nbmodel.txt", "r", encoding="latin1")
for line in name:
    if count == 0:
        s = line.split(" ")
        spamP = float(s[0])
        count+=1
        continue
    if count == 1:
        s = line.split(" ")
        hamP = float(s[0])
        count+=1
        continue    
    if "Spam Prob" in line:
        sBool = True
        print ("Reached")
        continue
    arg = line.split(" ")
    if sBool:
        spamDict[arg[0]] = arg[1]
    else:
        hamDict[arg[0]] = arg[1]

classifiedSpam = 0
correctSpam = 0
trueHam = 0
trueSpam = 0
classifiedHam = 0
correctHam = 0
output = open("nboutput.txt","w")
for root, subdirs, files in os.walk(filename):
        os.chdir(root)
        for file in glob.glob("*.txt"):
            hamProb = 0
            spamProb = 0
            with open(file, "r", encoding="latin1") as f1:
                if "ham" in root:
                    trueHam +=1
                if "spam" in root:
                    trueSpam +=1
                for line in f1:
                    wordlist = line.split()
                    for word in wordlist:
                        if word in hamDict:
                            hamProb += math.log(float(hamDict[word]))
                            spamProb += math.log(float(spamDict[word]))
                hamProb += math.log(hamP)
                spamProb += math.log(spamP)
                if(hamProb>spamProb):
                    output.write("ham "+os.path.join(root,file)+ "\n")
                    if "ham" in root:
                        correctHam += 1
                    classifiedHam +=1
                else:
                    output.write("spam "+os.path.join(root,file)+ "\n")
                    if "spam" in root:
                        correctSpam += 1
                    classifiedSpam +=1
hamPrec = (correctHam/classifiedHam)
spamPrec = (correctSpam/classifiedSpam)
hamRecall = (correctHam/trueHam)
spamRecall = (correctSpam/trueSpam)
f1spam = (2*spamRecall*spamPrec)/(spamPrec+spamRecall)
f1ham = (2*hamRecall*hamPrec)/(hamPrec+hamRecall)

print (str(correctSpam/classifiedSpam))  #spam precision
print (str(correctSpam/trueSpam))       #spam recall
print(str(f1spam))      #f1spam
print (str(correctHam/classifiedHam))  #ham precision
print (str(correctHam/trueHam))         #ham recall   
print(str(f1ham))       #f1ham  
