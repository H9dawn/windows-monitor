import os
import re
import time
import difflib

serviceReg = '(SERVICE_NAME.*?)\n'
a = os.popen('sc query').read()
aList = re.findall(serviceReg,a)
whiteList = aList


def bServiceScan():
	global aList
	global whiteList
	b = os.popen('sc query').read()
	bList = re.findall(serviceReg,b)
	diffInstance = difflib.Differ()
	diffList = list(diffInstance.compare(aList,bList))
	if len(aList) != len(bList):
		for i in diffList:
			if i[0] == '-' or i[0] == '+':
				if i[2:] not in whiteList:
					print("变化的服务：")
					print(i)
					print()
	return bList

def serviceScan():
	global aList
	bList = bServiceScan()
	aList = bList


if __name__ == '__main__':
	while True:
		serviceScan()
