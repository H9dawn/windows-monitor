import os
import re
import time
import difflib

processReg = '(.*?)  '
processReg1 = ' (.*?)  '#靠，搞半天是正则的问题
a = os.popen('tasklist /V').read()
aList = a.split("\n")[3:]#0是空  1是标题  2是横线  3才开始
whiteList = []
for i in aList:
	result = re.findall(processReg,i)
	if result != []:
		if result[0] not in whiteList:
			whiteList.append(result[0])

def bProcessScan():
	global aList
	global whiteList
	b = os.popen('tasklist /V').read()
	bList = b.split("\n")[3:]
	diffInstance = difflib.Differ()
	diffList = list(diffInstance.compare(aList,bList))
	if len(aList) != len(bList):
		for i in diffList:
			if i[0] == '-' or i[0] == '+':
				result = re.findall(processReg1,i)
				if result != [] :
					if result[0] not in whiteList:
						print("变化的进程：")##这里还有点问题，sc一直在用（services的），导致这里一直在变，需要再加白名单
						print(i)
						print()
	return bList

def processScan():
	global aList
	bList = bProcessScan()
	aList = bList


if __name__ == '__main__':
	while True:
		processScan()
