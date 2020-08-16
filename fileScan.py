import os
import hashlib
import time
import re
import difflib

#测试阶段，先把目录写死一下 E:\phpstudy\phpstudy_pro\WWW\count
dir = 'E:\phpstudy\phpstudy_pro\WWW\count'
aList = []
for root, dirs, files in os.walk(dir, topdown=False):
	for file in files:
		aList.append(os.path.join(root, file))
'''
def Hash(filepath):#hash计算方法可自行修改，试过自带的hash()函数，发现每次结果都不一样- -
	with open(filepath, 'rb') as f:
		file = f.read()
		md5obj = hashlib.md5()
		md5obj.update(file)
		hash = md5obj.hexdigest()
	return filepath + " Hash被修改：" + hash
'''
def fileScan():
	global aList
	bList = []
	for root, dirs, files in os.walk(dir, topdown=False):#top -- 根目录下的每一个文件夹(包含它自己)
	#产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】。
	#topdown --可选，为True或者没有指定, 一个目录的的3-元组将比它的任何子文件夹的3-元组先产生 (目录自上而下)。
	#如果topdown为 False, 一个目录的3-元组将比它的任何子文件夹的3-元组后产生 (目录自下而上)。
		#print(files) 发现py2和py3是有区别的，py2的files不包含子目录下的，谨记
		for file in files:
			bList.append(os.path.join(root, file))
	if len(aList) != len(bList):
		diffInstance = difflib.Differ()
		diffList = list(diffInstance.compare(aList,bList))
		for i in diffList:
			if i[0] == '-' or i[0] == '+':
				print("变化的文件：")
				print(i)
		print()
	aList = bList
	

if __name__ == '__main__':
	while True:
		fileScan()
