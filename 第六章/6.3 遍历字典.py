####遍历所有的键-值对####

user_0 = {
    'user_name':'efermi',
    'first':'enrico',
    'last':'fermi'
}
for key,value in user_0.items():       ########声明两个变量用来存储键和值######## .item()返回键=值对列表##########
    print("\nkey: " + key)
    print("value: " + value)

####遍历字典中的所有键####

favorite_languages = {
    'jen':'python',
    'sarah':'C',
    'edward':'ruby',
    'phil':'python'
}
friends = ['phil','sarah']
for name in favorite_languages.keys():          ######## keys()不适用字典中的值，只使用键##########
    print(name.title())                         ########## 默认遍历所有键，所以不输入keys()也没问题#####
    if name in friends:
        print(" Hi " + name.title() + ",I see your favorite language is " + favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():        ####确定某个人是否接受了调查####
    print("Eric,please take our poll!")

####按顺序遍历字典中的所有键####

favorite_languages = {
    'jen':'python',
    'sarah':'C',
    'edward':'ruby',
    'phil':'python'
}
for name in sorted(favorite_languages.keys()):                ####调用sorted()对列表进行排序####
    print(name.title() + ",thank you for taking the poll.")

####遍历字典中的所有值####

favorite_languages = {
    'jen':'python',
    'sarah':'C',
    'edward':'ruby',
    'phil':'python'
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):         ####调用values()返回值列表而不返回键####set()剔除掉重复元素####
    print(language.title())