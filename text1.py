#--*-- coding:gbk --*--


#��ϰ����
#print(5+3)
#print(10-2)
#print(2*4)
#print(16/2)

#���Ժ���str
#fav_number = 12
#print("My favorite number is " + str(fav_number) + " !\n")

 

#�����б�����
#bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#print(bicycles[0].title())

#�б���ϰ�ļ�

#names = ['liwen','elliot','jhon','tom']
names.append('lina')
names.insert(2,'blak')
print(names)
#i=0
#while i<5:
#	print("Hello " + names[i].title() + "!")
#	i=i+1

while len(names) > 2:
	poped_name = names.pop()
	print("Sorry, " + poped_name + ", I couldn't dinner with you.")
print(names)
	
