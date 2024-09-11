luck_number=8 #创建一个整形变量luck_number,并为其赋值

my_name='menjinyan' #字符串类型的变量
print('luck_number的数据类型是',type(luck_number))
print(my_name,'的幸运数值是:',luck_number)

#python动态修改变量的数据类型，通过赋不同类型的值可以直修改
luck_number='北京欢迎你'
print('luck_number的数据类型是:',type(luck_number)) #<class 'str'>

#在python当中允许多个变量指向同一个值
no=number=1024 #no与number都指向1024这个数值
print(no,number)
print(id(no)) #id()查看对象的内存地址的253525366736
print(int(number))# 253525366736