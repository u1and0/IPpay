'''
## IPpay ver1.0

__UPDATE1.0__
First commit

__USAGE__
Just build

__INTRODUCTION__
IP電話アプリの料金をグラフ化

__ACTION__
http://s-dentoku.mobile-runner.com/hikaku
の料金をグラフ化してくれる
planに料金表


__TODO__
携帯と固定電話を別々にグラフ化
'''





timeSec=[i for i in range(360)]
plan={'050plus':[300,9,29,60],
		'fusionIP':[0,8,8,30],
		'LaLa Call':[100,6,28,60],
		'G-Call050':[280,5,10,60],
		'050Call':[0,2,2,60],
		'050free':[0,3.99,4.33,60],
		'ServersMan 050':[300,7.5,40,180],
		'BIGLOBEフォン・モバイル':[300,8,30,60],
		'FleaLine Light':[400,8,30,60],
		'BlueSIPフォン':[600,21,21,60]
		}




# pay=[ for i in ]
# print(timeSec)
k=0
for sev in plan.keys():
	j,cell,fix=0,[],[]
	for i in timeSec:
		cell.append(plan[sev][0]+plan[sev][1]*j)
		fix.append(plan[sev][0]+plan[sev][2]*j)
		if i%plan[sev][3]==0:j+=1
	plan[sev].append(cell)
	# plan[sev].append(fix)
	print(plan[sev][4])
	# print(plan[sev][5])
	k+=1
	import matplotlib.pyplot as plt
	dashtype='-' if k<7 else '--'
	plt.plot(list(map(lambda re: re/60,timeSec)),plan[sev][4],dashtype,label=sev+' cell')
	# plt.plot(list(map(lambda re: re/60,timeSec)),plan[sev][5],label=sev+' fix')
plt.legend(bbox_to_anchor=(1, 1), loc='best', borderaxespad=0,fontsize='small')
plt.subplots_adjust(right=0.75)
plt.xlabel('minuits')
plt.ylabel('Yen')
plt.show()


