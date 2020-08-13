
lines = []
with open('3.txt', 'r',encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())
		#print(lines)

for line in lines:
	
	
	s = line.split(' ')
	#print(s)
	name_and_time = s[0]
	#print(name_and_time)
	time = name_and_time[0:5]
	#print(time)
	name = name_and_time[5:]
	#print(name)
	sentence = s[1:]
	print(sentence)

