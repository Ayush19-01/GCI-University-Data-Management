from pyexcel_ods import get_data
import json
data = get_data("Data1.ods")
dict1={}
x=json.dumps(data)
x=eval(x)
def prRed(skk): return str("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): return str("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): return str("\033[93m {}\033[00m" .format(skk)) 
def prPurple(skk): return str("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): return str("\033[96m {}\033[00m" .format(skk)) 
for i in x:
	for j in  x[i]:
		tmpint=0
		if len(j)>1 and type(j[1])==type(1):
			for k in range(1,8):
				if k==1 or k==5:
					tmpint+=j[k]
					tmpint+=j[k]
				else:
					tmpint+=j[k]
			dict1[j[0]]=round(tmpint/9,2)
	
data = get_data("Data2.ods")
dict2={}
x=json.dumps(data)
x=eval(x)
for i in x:
	for j in  x[i]:
		tmpint=0
		if len(j)>1 and type(j[1])==type(1):
			for k in range(1,8):
				if k==1 or k==5:
					tmpint+=j[k]
					tmpint+=j[k]
				else:
					tmpint+=j[k]
			dict2[j[0]]=round(tmpint/9,2)

data = get_data("Data3.ods")
dict3={}
x=json.dumps(data)
x=eval(x)
for i in x:
	for j in  x[i]:
		tmpint=0
		if len(j)>1 and type(j[1])==type(1):
			for k in range(1,8):
				if k==1 or k==5:
					tmpint+=j[k]
					tmpint+=j[k]
				else:
					tmpint+=j[k]
			dict3[j[0]]=round(tmpint/9,2)
			
data = get_data("Data4.ods")
dict4={}
x=json.dumps(data)
x=eval(x)
for i in x:
	for j in  x[i]:
		tmpint=0
		if len(j)>1 and type(j[1])==type(1):
			for k in range(1,8):
				if k==1 or k==5:
					tmpint+=j[k]
					tmpint+=j[k]
				else:
					tmpint+=j[k]
			dict4[j[0]]=round(tmpint/9,2)

dict5={}
for i in dict1:
	z=0
	z+=dict1[i]
	z+=dict2[i]
	z+=dict3[i]
	z+=dict4[i]
	z=round((((z/4)*4)/10),2)
	dict5[i]=z


data = get_data("IELTS.ods")
dict6={}
x=json.dumps(data)
x=eval(x)
for i in x:
	for j in  x[i]:
		tmpint=0
		if len(j)>1 and type(j[1])==type(1):
			for k in range(1,5):
				tmpint+=j[k]
			dict6[j[0]]=round((((((tmpint/4)/9)*100)*30)/100),2)
		if len(j)>1 and type(j[1])==type(1.0):
			for k in range(1,5):
				tmpint+=j[k]
			dict6[j[0]]=round((((((tmpint/4)/9)*100)*30)/100),2)

data = get_data("Interview.ods")
dict7={}
x=json.dumps(data)
x=eval(x)
for i in x:
	for j in  x[i]:
		tmpint=0
		if len(j)>1 and type(j[1])==type(1):
			for k in range(1,6):
				tmpint+=j[k]
			dict7[j[0]]=round(((((tmpint/5)*10)*30)/100),2)

total=0
dict8={}
for i in dict5:
	xt=dict5[i]
	yt=dict6[i]
	zt=dict7[i]
	total=xt+yt+zt
	dict8[i]=round(total,2)

dict9={}
list1=[]
for i in dict8:
	tmp=dict8[i]
	dict9[tmp]=i
	list1.append(tmp)
list1.sort()
list1.reverse()
list2=[]
intvar=1
print("")
print("{:22}{:28}{}".format(prRed("Rank"),prRed("Name"),prRed("Overall Score(Includes 40% Academics, 30% IELTS and 30% Interview)")))
print("")
for i in list1:
	xmain=dict9[i]
	tmpstr="  {:18}{:58}{}".format(prPurple(str(intvar)),prYellow(xmain),prCyan(str(i)+" %"))
	print(tmpstr)
	intvar+=1
	print("")
	
	
	