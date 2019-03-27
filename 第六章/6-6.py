favorite_languages = {
    'jen':'python',
    'sarah':'C',
    'edward':'ruby',
    'phil':'python'
}
names = ['jen','sarah','rxrn','zw','cc']
for name in names:
    if name in favorite_languages.keys():
        print(name.title() + " ,thank you for inviting the survey!")
    else:
        print(name.title() + " ,welcome you invite my survey!")