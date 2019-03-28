cities = {
    'newyork':{
        'country':'us',
        'population':'10000000',
        'fact':'the biggest city in US'
    },
    'beijing':{
        'country':'china',
        'population':'20000000',
        'fact':'capital city in china'
    },
    'hongkong':{
        'country':'china',
        'population':'7000000',
        'fact':'econimical center'
    },
}
for city,message in cities.items():
    country = message['country']
    population = message['population']
    fact = message['fact']
    print('\n\tcity: ' + city.title())
    print("\tcountry: " + country.title())
    print("\tpopulation: " + population.title())
    print("\tfact: " + fact.title())