'''1、列表中的每一个元素都是可以变的
   2、列表中的元素都是有序的，也就是说每一个元素都有一个位置
   3、列表可以容纳Python中的任何对象'''

fruit = ['Apple','Orange','pear']
fruit.insert(1,'grape') #在第二个数据前面插入
print(fruit)
fruit.remove('pear')    #删除
print(fruit)
fruit[0] = 'Grapefruit' #替换
print(fruit)