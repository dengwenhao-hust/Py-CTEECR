# -*- coding: utf-8 -*-
"""
first Created on Wed Oct 24 20:56:04 2018
Modified on Wed Nov 10 20:28:22 2021
@author: hust_liao_group_members
"""

from time import time
import sys
t0=time()

pypath = sys.path[0]
FolderPath= pypath + '/'  #读取文件当前目录
ChangeFile='within10-residue.pdb'   #活性区10埃之内的pdb文件，该文件末尾不能有空行

import csv
import sys
import re
import os
import shutil

maxInt = sys.maxsize
decrement = True
'''
这一步是扩容
''' 
while decrement:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.
 
    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt / 10)
        decrement = True

'''
读取10A残基文件
'''
with open(FolderPath+ChangeFile,encoding='utf-8') as mainDict:
    headers=csv.reader(mainDict)
    data = list(headers)
    
    test=[]
    index_number=[]
    index_acid=[]

    
    for i in range(len(data)-1):
    
        k=re.split(r'\s',data[i][0])
        while '' in k:
            k.remove('')
        
        index_number.append(int(k[1]))
        index_acid.append(k[3].lower()+'-'+k[10].lower()+'-'+k[4].lower())    
            
        test.append(k)


empty='   '        
default_name='thr-enzb-153' #需要修改：153为第一个被删除thr的residue编号
NameFile='5ymr-cs-reaction' #需要修改chm文件名字
ChargeFile='save_5ymr-cs-reaction' #修改save_chm文件名  
chargeData=[] 
chargeData_duplicate=[] 
name=0
java_draft='/home/liao-312/software/chemsh/chemsh-3.7.0/scripts/chemsh <'  #此处为chemshell运行命令，需准确提供chemshell安装路径

with open(FolderPath+ChargeFile+'.chm',encoding='utf-8') as oriCharge:           
    headers=oriCharge.readlines()
    datum=list(headers)
    for i in range(len(datum)):
        chargeData.append(datum[i])
        chargeData_duplicate.append(datum[i])


with open(FolderPath+'qchemsh.pbs',encoding='utf-8') as java:
    headers=java.readlines()
    java_data=list(headers)
    
with open(FolderPath+NameFile+'.chm',encoding='utf-8') as oriName:
    headers=oriName.readlines()
    data=list(headers)
    for i in range(1):
        print(data[9])
        a='aaaa'+'cccc'
        temp='%s'% data[9][-1]#+'-'+index_acid[i]
        
        like=data[9][:-1]+'-'+index_acid[name]+temp
        data[9]=like
        
        path=FolderPath+'/'+NameFile+'-'+index_acid[i]
        for i in range(len(java_data)):
            if i == 34:
                java_data[i]=java_draft+NameFile+'-'+index_acid[0]+'.chm >& '+NameFile+'-'+index_acid[0]+'.log '  #进行qchemsh提交作业命令的修改
            else:
                pass

#开始进行文件复制
        os.makedirs(path) 
        
        with open(path+'/'+NameFile+'-'+index_acid[name]+'.chm','w') as a:
            a.writelines(data)
            
        shutil.copyfile(FolderPath+'alpha',path+'/'+'alpha') 
        shutil.copyfile(FolderPath+'basis',path+'/'+'basis') 
        shutil.copyfile(FolderPath+'beta',path+'/'+'beta') 
        shutil.copyfile(FolderPath+'control',path+'/'+'control') 
      
        shutil.copyfile(FolderPath+NameFile+'.psf',path+'/'+NameFile+'-'+index_acid[name]+'.psf')
        shutil.copyfile(FolderPath+NameFile+'.pdb',path+'/'+NameFile+'-'+index_acid[name]+'.pdb')                
        shutil.copyfile(FolderPath+NameFile+'.c',path+'/'+NameFile+'-'+index_acid[name]+'.c')  
        
        with open(path+'/'+'qchems.pbs','w') as a:
            a.writelines(java_data)        
#开始进行第一个residue电荷删除
for name in range(len(index_acid)):
    if index_acid[name]==default_name:
        i = index_number[name]
        c=re.findall(r"\d+\.?\d",chargeData[i])
        chargeData[i]=float(c[0])
        chargeData[i]=0.0
        chargeData[i]=str(chargeData[i])
        chargeData[i]=empty+chargeData[i]+'0000\n'       
#开始进行后续所有residues电荷删除和文件复制    
    else:    
        with open(FolderPath+NameFile+'.chm','r') as oriName:
            headers=oriName.readlines()
            data=list(headers)
            for i in range(1):
                print(data[9])
                
                temp='%s'% data[9][-1]#+'-'+index_acid[i]
                like=data[9][:-1]+'-'+index_acid[name]+temp
                data[9]=like
                path=FolderPath+NameFile+'-'+index_acid[name]
                os.makedirs(path) 
                shutil.copyfile(FolderPath+'alpha',path+'/'+'alpha') 
                shutil.copyfile(FolderPath+'basis',path+'/'+'basis') 
                shutil.copyfile(FolderPath+'beta',path+'/'+'beta') 
                shutil.copyfile(FolderPath+'control',path+'/'+'control') 
              
                shutil.copyfile(FolderPath+NameFile+'.psf',path+'/'+NameFile+'-'+index_acid[name]+'.psf')
                shutil.copyfile(FolderPath+NameFile+'.pdb',path+'/'+NameFile+'-'+index_acid[name]+'.pdb')                
                shutil.copyfile(FolderPath+NameFile+'.c',path+'/'+NameFile+'-'+index_acid[name]+'.c')   
            
                with open(path+'/'+NameFile+'-'+index_acid[name]+'.chm','w') as a:
                    a.writelines(data)                    

                    
                for i in range(len(java_data)):
                    if i == 34:
                        java_data[i]=java_draft+NameFile+'-'+index_acid[name]+'.chm >& '+NameFile+'-'+index_acid[name]+'.log ' #34是qchemsh的文件最后一行，这里修改交作业的名字
                    else:
                        pass
                with open(path+'/'+'qchems.pbs','w') as a:
                    a.writelines(java_data) 
                           
        with open(FolderPath+NameFile+'-'+default_name+'/'+ChargeFile+'-'+default_name+'.chm','w') as oriCharge:
            oriCharge.writelines(chargeData)
        
        chargeData=[]
        print(chargeData)
        for l in range(len(chargeData_duplicate)):
            chargeData.append(chargeData_duplicate[l])

        
        default_name=index_acid[name]

        i = index_number[name]
        c=re.findall(r"\d+\.?\d",chargeData[i])
        chargeData[i]=float(c[0])
        chargeData[i]=0.0
        chargeData[i]=str(chargeData[i])
        chargeData[i]=empty+chargeData[i]+'0000\n'        
        
    if name == len(index_acid)-1:      
        with open(FolderPath+NameFile+'-'+index_acid[name]+'/'+ChargeFile+'.chm','w') as oriCharge:
            oriCharge.writelines(chargeData)
    else:
        pass   
 