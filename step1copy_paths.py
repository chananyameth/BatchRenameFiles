#only applys tp this specipic folder (with one subfolder, and wanting ch rename just ROOT files (NOT the sub-folder ones))

import os
file = open('sourcePaths.txt', 'r+')
a,b = os.walk(r'C:\Users\Chananya\Desktop\pics vacation 2020\pics')    #real one
#a,b = os.walk(r'C:\a\a')   #example
path = a[0]
filesList = a[2]
for l in filesList:
	file.write(str(l)+','+str(l)+'\n')
file.close()

input('format: src,dst. change only dst.\nDO NOT REMOVE LAST LINE!!!\n\npress enter to rename.')

file = open('sourcePaths.txt', 'r+')
for line in file:
	line=line[0:-1]
	src,dst = line.split(',')
	os.rename(path+'\\'+src,path+'\\'+dst)
file.close()