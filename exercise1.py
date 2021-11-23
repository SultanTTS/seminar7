try:
	fhand=open('brown.txt')
except:
	print('File cannot be opened:', fhand)
	exit()
lines=fhand.readlines()
fhand.close()
dict1={}
fhand2=open('output.txt','w')

for line in lines:
	words=line.split()
	length=len(words)

	for i in range(length-2):
		key=words[i]+' '+words[i+1]+' '+words[i+2]
		if key not in dict1:
			dict1[key]=1
		else:
			dict1[key]+=1

max=None
for key in dict1:
	result=key,dict1[key]
	fhand2.write(str(result))
	fhand2.write('\n')
	if max is None or dict1[key]>max:
			max=dict1[key]
print('max:',max)

