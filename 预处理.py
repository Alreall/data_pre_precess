import pandas as pd
import os
import csv

lane = "东西819"

#将单个txt文件保存成一个
#获取目标文件夹的路径
filedir = ("P:/raocheng4/%s"%lane)
#获取当前文件夹中的文件名称列表
filenames=os.listdir(filedir)
filenames.sort()
#print(filenames)
#打开当前目录下的result.txt文件，如果没有则创建

f=open('result_%s.txt'%lane,'w')
#先遍历文件名
for filename in filenames:
    filepath = filedir+'/'+filename
    #遍历单个文件，读取行数
    filename = filename[:-4]    #为数据添加时间戳
    for line in open(filepath):
        f.writelines(filename+" "+line)
    #    f.write('\n')
#关闭文件
f.close()

#将空格分割的文件转换为逗号分割的csv
csvFile = open("data_%s.csv"%lane, 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(csvFile)
csvRow = []
f = open("result_%s.txt"%lane, 'r')

for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()
#,"longitude","latitude","altitude","lane"
#给数据添加标签
df = pd.read_csv("data_%s.csv"%lane)
df.columns=(["time","tra_ID","type","conf","age","x","y","z","length","width","height","dir_x",
            "dir_y","dir_z","anc_x","anc_y","anc_z","v_x","v_y","v_z",
            "a_x","a_y","a_z"])#,"longitude","latitude","altitude","lane"
df["time_s"] = (df["time"]-df['time'].min())/1000
#df['position_m']=(df['position']-df['position'].min())
#max = df['tra_ID'].values[-1]
df.to_csv("P:/raocheng4/initial%s.csv"%lane, encoding='utf-8-sig')