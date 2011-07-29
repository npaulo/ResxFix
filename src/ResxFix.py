import re
import sys
import os
import stat

filePath = sys.argv[1];
filename = os.path.basename(filePath)
dirpath = os.path.dirname(filePath)

bkOutputFile = dirpath + os.sep + 'bk' + filename

fin = open( filePath, "r" )
fileContent = fin.read()
fin.close()

basename = os.path.basename( filePath )

contentToParse = fileContent
resultContentFile = ""

if re.search(r"j00LjAuMC4w",contentToParse, 1):
	print "RESX BUG found in file <%s>... processing"%(filePath)
	
	'''step 1'''
	regexImageStream = re.compile(r"<data.+\".+\.ImageStream\".+mimetype=\".+\.base64\"")
	'''step 2'''
	regexValue = re.compile(r"<value>")
	'''step 3 bug finded'''
	regexBug = re.compile(r"j00LjAuMC4w$")
	
	step = 1
	fin = open( filePath, "r" )
	fout = open(bkOutputFile, "w")
	
	while 1:
		line = fin.readline()
		if not line:
			break
		
		if step == 1 and regexImageStream.search(line):
			step = 2
		elif step == 2 and regexValue.search(line):
			step = 3
		elif step == 3:
			line = regexBug.sub(r"j0yLjAuMC4w", line)
			step = 1
		
		fout.write(line)
		
	fin.close()
	fout.close()
	
	os.chmod(filePath, 128) 
	os.remove(filePath)
	os.rename(bkOutputFile, filename)
	
	print "RESX BUG in file <%s> is FIXED."%(filePath)

else:
	print "File <%s> is OK."%(filePath)