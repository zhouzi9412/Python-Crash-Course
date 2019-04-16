def city_country(city_name, city_country):
    """城市的名字和国家"""
    city_details = city_name + ' ' + city_country
    return city_details.title()
musician = city_country('beijing','china')
print(musician)
