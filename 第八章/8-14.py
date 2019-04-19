def make_car(brand, location, **user_info):
    profile ={}
    profile['brand_name'] = brand
    profile['location_name'] = location
    for key, value in user_info.items():
        profile[key] = value
    return profile

print_car = make_car('subaru', 'outback',color='blue', tow_package=True)
print(print_car)