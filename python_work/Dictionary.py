alien_0 = {'color': 'green', 'points': 5}       #字典用键值对来存储信息
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['speed'] = 'slow'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment     #根据外星人速度确定位置

#del alien_0['points']       删除键值对

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'java',
}       #由类似对象组成的字典

point_value = alien_0.get('points', 'No point value assigned.')
time_value = alien_0.get('time', 'No point value assigned.')        #使用get方法防止使用了字典中不存在的键值对
print(point_value)
print(time_value)

for k, v in alien_0.items():        #遍历字典中的键值对
    print(k)
    print(v)
for name in favorite_languages.keys():      #只遍历键
    print(name)
if 'erin' not in favorite_languages.keys():     #keys()方法实际上返回的是一个包含字典中所有键的列表
    print("Erin, please take our poll!")
