####字典是一系列键：值的对儿，每个键与一个值关联，使用键访问值####

####访问字典中的值####

alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + "points!")

####添加键——值对####

alien_0 = {'color':'green','points':5}
print(alien_0)
alien_0['x_position'] = 0                      #######直接添加即可#######
alien_0['y_position'] = 25
print(alien_0)

####先创建一个空字典####

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)               ######使用字典存储用户数据或者编写自动生成键值得代码时，一般需要定义空字典#######

####修改字典中的值####

alien_0 = {'color':'green'}
print("The alien is" + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

####对不同速度移动的外星人进行跟踪####

alien_0 = {'x_position': 0,'y_position':25,'speed':'medium'}
print("Original x_position: " + str(alien_0['x_position']))
#向右移动外星人
#据外星人当前速度决定其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #这个外星人速度一定很快
    x_increment = 3
#新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

####删除键-值对####

alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

####由类似对象组成的字典####

favorite_languages = {
    'jen':'python',
    'sarah':'C',
    'edward':'ruby',
    'phil':'python'
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")