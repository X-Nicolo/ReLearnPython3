# list的使用
classmates = ["Nicolo","Tom","Jerry"]
print("从开始取：",classmates[0])
print("从末尾取：",classmates[-1])
print("获取list的长度：",len(classmates))
classmates.append('Adam')
print("list中追加元素到末尾：",classmates[-1])
classmates.insert(1, 'Jack')
print("按照索引插值：",classmates[1])
print("要删除list末尾的元素，用pop()方法,删除的东西",classmates.pop())
print("要删除指定位置的元素，用pop(i)方法，其中i是索引位置：", classmates.pop(1))
print("要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：")
classmates[1] = 'Sarah'
print(classmates)