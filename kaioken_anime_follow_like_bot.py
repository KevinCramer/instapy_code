
from instapy import InstaPy
from instapy import smart_run

my_list = []
with open('junpei_anime_current_list_to_follow.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        my_list.append(currentPlace)




# login credentials

insta_username = 'kaioken.anime'
insta_password = 'n3v3rg!veuP'


# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    
    session.follow_by_list(followlist = my_list[0:30],sleep_delay = 0)
    session.like_by_users(my_list[0:30], amount=3)

my_list = my_list[30:]

with open('junpei_anime_current_list_to_follow.txt', 'w') as filehandle:
    for listitem in my_list:
        filehandle.write('%s\n' % listitem)


