list1 = []
list2 = []
print(list1)
print(list1[0])
print(list1[-1])        #倒数第一个元素，以此类推
list1.append('')
list1.insert(0, '')      #索引+值
del list1[0]
list1.pop(0)     #弹出某位置元素并返回其值
list1.remove('')        #根据元素值删除元素
list1.sort(reverse=True)        #永久排序/排倒序
sorted(list1, reverse=True)     #输出排序后的结果但是不影响原本列表元素的顺序
list1.reverse()
len(list1)

for list in list1:      #循环
    print(list)

for value in range(1, 5):
    print(value)

even_numbers = list(range(2, 11, 2))        #1-10的偶数
min(even_numbers), max(even_numbers), sum(even_numbers)

squares = [value**2 for value in range(1, 11)]      #平方数

print(list1[0:3])       #打印前三个元素        使用切片可以复制列表
for list in list1[:3]:
    print(list)

dimensions = (200, 50)      #元组，其中元素不可修改
