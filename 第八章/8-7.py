def make_album(actor_name, album_name, numbers=''):
    """描述音乐专辑"""
    if numbers:
        album_details = actor_name + ' ' + album_name + ' ' + numbers
    else:
        album_details = actor_name + ' ' + album_name
    return album_details.title()
while True:
    print("\nPlease tell me the album's details: ")
    print("(enter 'q' at any time to quit)")
    ac_name = input("actor name: ")
    if ac_name == 'q':
        break
    al_name = input("album name: ")
    if al_name == 'q':
        break
    num = input("song numbers: ")
    if num == 'q':
        break
    message = make_album(ac_name, al_name, num)
    print(message)