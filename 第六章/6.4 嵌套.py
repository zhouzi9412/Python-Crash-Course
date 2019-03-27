####将一系列字典存储在列表中，或将列表作为值存储在字典中叫嵌套####
####列表中可以嵌套字典，字典中也可嵌套列表####

####字典列表####

alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

#### 用range自动生成####

#创建一个用于存储外星人的空列表
aliens = []
#创建30个绿色的外星人
for alien_number in range(30):                              ####range()告诉重复多少次循环####
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)                                ####每次循环都创建个外星人，并附加在aliens末尾####
for alien in aliens[0:3]:                                    ####外星人变色且移动速度加快####
    if alien['color'] == 'green':
        alien['color'] == 'yellow'
        alien['speed'] == 'medium'
        alien['points'] == 10
    elif alien['color'] == 'yellow':                        ####将黄色外星人改为移动速度更快且分数更高的红色外星人####
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
#显示前五个外星人
for alien in aliens[:5]:                                    ####切片，打印前5个外星人####
   print(alien)
print("...")
#显示创建了多少个外星人
print("Total number of aliens:" + str(len(aliens)))

####在字典中储存列表####

#存储所点比萨的值
pizza = {
    'crust':'thick',
    'toppings':['mushroom','extra cheese'],
}
#概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza" + " with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

####值为列表时，主要在使用一个循环来遍历列表####

favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}
for name,languages in favorite_languages.items():
    if len(languages) < 2:
        for language in languages:
            print("\n" + name.title() + " only like " + language.title() + ".")
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())

####在字典中存储字典####

####网站用户信息，用户名为键，信息存储在一个字典中，这个字典作为值，形成字典嵌套####

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}
for username,user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())