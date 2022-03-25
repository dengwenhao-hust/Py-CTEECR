# -*- coding: utf-8 -*-
"""
First Created on Sat Nov  3 18:56:50 2018
Modified on Wed Nov 11 10:19:54 2021
@author: hust_liao_group_members
"""

import os
import re
import sys

path=os.listdir(os.getcwd())
folderpath=os.getcwd()+'/'
#遍历文件夹，搜索log
def outputlog(filepath):
    log_name=''
    for name in os.listdir(filepath):
        if re.search('5ymr',name):     #选取log文件命名的一个关键字
            if re.search('log',name):
                log_name=name
    return log_name
#遍历文件夹，搜索log的数据
def output_energy(fold,filename):
    with open(folderpath+fold+'/'+filename,'r') as data:
        headers=data.readlines()
        datum=list(headers)
        for i in range(len(datum)):
            if re.search('Contribution to energy from                  turbomole',datum[i]):
                QM=re.findall(r"\d+\.?\d",datum[i])
            if re.search('Contribution to energy from                    dl_poly',datum[i]):
                MM=re.findall(r"\d+\.?\d",datum[i])
            if re.search('QM/MM Energy:                                         ',datum[i]):
                QM_MM=re.findall(r"\d+\.?\d",datum[i])
    return QM,MM,QM_MM

main_log=[['name of residule','QM','MM','QM/MM']]
#统计数据       
for p in path :
		if os.path.isdir(p):
				print(p)
				empty=[]
				empty.append(p)
				c=outputlog(p)
				qm,mm,qm_mm = output_energy(p,c)
				empty.append('-'+qm[0]+qm[1])
				empty.append('-'+mm[0]+mm[1])
				empty.append('-'+qm_mm[0]+qm_mm[1])
				main_log.append(empty)

#输出csv
with open (folderpath+'sum_data_file'+'.csv','w') as a:
    for lines in range(len(main_log)):
        for sin in range(len(main_log[lines])):
            a.write(main_log[lines][sin])
            a.write(',')
        a.write('\n')




