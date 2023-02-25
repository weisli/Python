#--*-- coding:gbk --*--


#复习测试
#print(5+3)
#print(10-2)
#print(2*4)
#print(16/2)

#测试函数str
#fav_number = 12
#print("My favorite number is " + str(fav_number) + " !\n")

 

#测试列表性能
#bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#print(bicycles[0].title())

#列表练习文件

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
	
