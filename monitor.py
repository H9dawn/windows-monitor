# -*- coding: utf-8 -*-
#该脚本启动后不会马上检测出来，需要等待一段时间，等初始化加载完成
#建议选择关键目录进行检测，不然太多太大检测不及时，卡死等问题，我到时候写一个敏感目录list
#本来想加优化的，比如不检查某些后缀的文件，但是感觉判断起来也挺耗时间的，也不知熟快熟慢

import portScan
import processScan
import serviceScan
import fileScan
import threading
		
if __name__ == '__main__':
	print("加载完毕：")
	while True:
		threads = []
		threads.append(threading.Thread(target=fileScan.fileScan))
		threads.append(threading.Thread(target=portScan.portScan))
		threads.append(threading.Thread(target=processScan.processScan))
		threads.append(threading.Thread(target=serviceScan.serviceScan))
		for i in threads:
			i.start()
		while threading.active_count() > 1:
			pass
