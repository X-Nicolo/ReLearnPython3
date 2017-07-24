# Python内置了字典：dict的支持，dict全称dictionary
# 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
# 这个通过key计算位置的算法称为哈希算法（Hash）。
# []：list
# ()：tuple
# {}: dict

# 学生成绩
score = {"Nicolo":100,"Tom":99,"Jerry":99}
print("打印Nicolo的成绩：",score["Nicolo"])
# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
score["Nicolo"] = 101
print("打印Nicolo的成绩：",score["Nicolo"])

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print("Nicolo" in score)
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
score.pop("Jerry")
print(score)

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s  = set([1,2,3])
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)
print(s)
# 通过remove(key)方法可以删除元素
s.remove(4)
print("移除后的",s)