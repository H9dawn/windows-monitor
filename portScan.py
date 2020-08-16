import os
import re
import time
import difflib

portReg = '(\d+.\d+.\d+.\d+)'
a = os.popen('netstat -ano | findstr "192.168" | findstr "ESTABLISHED | LISTENING | TIME_WAIT"').read()#过滤第一次
#写入白名单第二次，白名单为初始时的ip列表
aList = a.split("\n")#转成list
whiteList = []#初始启动时的白名单
for i in aList:
	result = re.findall(portReg,i)
	if len(result) == 2 :#有些是连的本地 *，只有一个结果，没必要继续了
		if result[1] not in whiteList:
			whiteList.append(result[1])

def bPortScan():
	global aList
	global whiteList
	b = os.popen('netstat -ano | findstr "192.168" | findstr "ESTABLISHED | LISTENING | TIME_WAIT"').read()
	bList = b.split("\n")
	diffInstance = difflib.Differ()
	diffList = list(diffInstance.compare(aList,bList))
	if len(aList) != len(bList):
		for i in diffList:
			if i[0] == '-' or i[0] == '+':
				result = re.findall(portReg,i)
				if result[1] not in whiteList:
					print("变化的连接：")
					print(i)
					print()
	return bList

def portScan():
	global aList
	bList = bPortScan()
	aList = bList
		

if __name__ == '__main__':
	while True:
		portScan()

	
	
