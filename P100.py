#-*- coding: utf-8 -*-
# coding: utf-8

import pandas as pd
import numpy as np

//pip install xlrd

//pip install xlwt

//import xlrd,xlwt

//data = xlrd.open_workbook('gzb.xlsx')

//pip install openpyxl

//import openpyxl

//wb = openpyxl.load_workbook('gzb.xlsx')

//wb.get_sheet_by_name('Sheet1')

//data = wb['Sheet1']

//print(data)

//df = list(data)

//print(df)

//dt = [item.value for item in list(data)[0]]

//print(dt)

//row1 =[item.value for item in list(data.rows)[0]]

//print(row1)

//DATA = pd.read_excel('gzb.xlsx')

DATA = pd.read_excel('gzb.xls')

print(DATA)

DATA[:31][:75]

DATA.iloc[:,1]

DATA.iloc[3,:]

import matplotlib.pyplot as plt

x = [DATA.iloc[7:11,1]]

print(x)

y = [DATA.iloc[7:11,74]]

print(y)

//plt.bar(str(x),y)
//plt.title('行业柱状图')
//plt.x_label('行业')
//plt.y_label('人数')
//pt.show()

plt.bar(['销售人员','专业人士','中高管人士','一般行政人员'],y[:])
plt.title('行业柱状图')
plt.x_label('行业')
plt.y_label('人数')
pt.show()

fig = plt.figure()
plt.bar(['sales','pros','chiefs','aministratos'],[0,48,19,4])
plt.title('field bar chart')
plt.xlabel('field')
plt.ylabel('counts')
plt.show()

fig = plt.figure()
plt.bar(['single','married,child','married'],[55,9,6])
plt.title('marrage bar chart')
plt.xlabel('marrage status')
plt.ylabel('counts')
plt.show()

x1 = np.linspace(1,31,31)
y1 = [0,3,3,6,3,3,3,9,9,12,9,9,6,6,3,0,0,0,3,6,3,3,6,3,3,3,6,6,3,3,3]
y2 = [0,0,0,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,0,0,0]

fig = plt.figure()
plt.plot(x1,y1)
plt.plot(x1,y2)
plt.title('Customer line chart')
plt.xlabel('days')
plt.ylabel('conts')
plt.legend(['Customer referral','Customer'])
plt.show()

x1 = np.linspace(1,31,31)
y1 = [1,1,0,1,0,0,1,1,1,2,2,0,2,2,3,0,4,1,3,3,3,1,4,1,1,0,1,1,1,1,3]
y2 = [0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,0]

fig = plt.figure()
plt.plot(x1,y1)
plt.plot(x1,y2)
plt.title('visit line chart')
plt.xlabel('days')
plt.ylabel('conts')
plt.legend(['Visits','Deals'])
plt.show()

agec = [5,1,0,64]
fig = plt.figure()
plt.pie(agec)
plt.title('Age pie chart')
plt.legend(['0-5','6-10','11-20','21+'])
plt.show()

P100 =

[25,25,23,25,19,24,25,27,24,26,28,26,26,26,24,21,27,24,26,25,28,23,23,23,25,25,25,24,24,2

6,25,25,26,25,26,18,18,22,22,22,22,23,22,28,20,23,24,23,23,26,23,24,26,24,26,23,23,23,23,

23,25,27,24,25,25,27,27,23,22,23]
P100c = [sum(np.array(P100)==19),sum(np.array(P100)==20),sum(np.array(P100)==21),sum

(np.array(P100)==22),sum(np.array(P100)==23),sum(np.array(P100)==24),sum(np.array(P100)

==25),sum(np.array(P100)==26),sum(np.array(P100)==27),sum(np.array(P100)==28)]
fig = plt.figure()
plt.pie(P100c)
plt.title('P100 pie chart, avg=24.16')
plt.legend(['19','20','21','22','23','24','25','26','27','28'])
plt.show()

xs =

[3,3,3,4,3,3,3,4,4,3,3,3,4,4,3,3,3,3,3,4,3,3,4,3,3,3,4,3,3,3,3,3,3,3,4,3,3,3,3,3,4,3,3,3,

3,4,4,3,3,3,4,4,3,3,3,3,3,4,3,3,4,3,3,3,4,3,3,3,3,4,3]
ys =

[2,3,2,2,2,3,2,2,2,2,2,2,4,2,2,2,2,3,2,4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,

2,2,2,2,2,2,2,5,2,2,2,2,2,5,2,2,2,3,2,2,2,2,2,2,2,3,2]
print(sum(np.array(xs)==3))
print((np.array(xs)==3)&(np.array(ys)==2))
s32 = sum((np.array(xs)==3)&(np.array(ys)==2))
print(s32)
s33 = sum((np.array(xs)==3)&(np.array(ys)==3))
print(s33)
s42 = sum((np.array(xs)==4)&(np.array(ys)==2))
print(s42)
s44 = sum((np.array(xs)==4)&(np.array(ys)==4))
print(s44)
s45 = sum((np.array(xs)==4)&(np.array(ys)==5))
print(s45)
fig = plt.figure()
plt.scatter(3,2,label='3-2',s=s32*1.5)
plt.scatter(3,3,label='3-3',s=s33*1.5)
plt.scatter(4,2,label='4-2',s=s42*1.5)
plt.scatter(4,4,label='4-4',s=s44*1.5)
plt.scatter(4,5,label='4-5',s=s45*1.5)
plt.title('Customer scatter chart')
plt.xlabel(['0-high scool','college','bachelor','master'])
plt.ylabel(['0-50000','50001-100000','100001-300000','300001-1000000','1000001+'])
plt.show()

xs = np.array(DATA.iloc[31,3:73])
ys = np.array(DATA.iloc[32,3:73])
s54 = sum((np.array(xs)==5)&(np.array(ys)==4))
print(s54)
s53 = sum((np.array(xs)==5)&(np.array(ys)==3))
print(s53)
s43 = sum((np.array(xs)==4)&(np.array(ys)==3))
print(s43)
s33 = sum((np.array(xs)==3)&(np.array(ys)==3))
print(s33)
s23 = sum((np.array(xs)==2)&(np.array(ys)==3))
print(s23)
fig = plt.figure()
plt.scatter(5,4,label='5-4',s=s54*2)
plt.scatter(5,3,label='5-3',s=s53*2)
plt.scatter(4,3,label='4-3',s=s43*2)
plt.scatter(3,3,label='3-3',s=s33*2)
plt.scatter(2,3,label='2-3',s=s23*2)
plt.title('Reachable scatter chart')
plt.xlabel(['not familiar','acknowledged','general','close'])
plt.ylabel(['very hard','hard','normal','easy'])
plt.show()
