from instapy import InstaPy
from instapy import smart_run
import sys

## if you type in the terminal python3 | follow.py | name (i.e yelena or junpei not yelena.anime nor junpei.anime)
##  | insta_password | num_follows | do_like? = yes/no (i.e do you want to like yes or no) | num_like (if so how many per user)
## that means it will follow num_follows  accounts and like each
## of their top num_like posts (assuming you set do_like? = yes) for the instagram account with username: name.anime
## and password: insta_password

if sys.argv[4] == 'yes' or sys.argv[4] == 'no':
    print (" You must either type yes or no")
    raise ValueError

num_people_follow = sys.argv[3]
num_likes_per_follow = sys.argv[5]
my_list = []
with open('{}_current_list.txt'.format(sys.argv[1]), 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        my_list.append(currentPlace)

new_my_list = my_list[num_people_follow:]

with open('{}_current_list.txt'.format(sys.argv[1]), 'w') as filehandle:
    for listitem in new_my_list:
        filehandle.write('%s\n' % listitem)

# login credentials

insta_username = '{}.anime'.format(sys.argv[1])
insta_password = sys.argv[2]
print('@@@@@@@@ I am following {} users, and liking their top {} posts @@@@@@@@@'.format(num_people_follow, num_likes_per_follow),file=sys.stderr)

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background

if  sys.argv[4] ==  'yes':
                  session = InstaPy(username=insta_username,
                  password=insta_password,
                  page_delay=5,
                  headless_browser=True)

                  with smart_run(session):
                      session.follow_by_list(followlist = my_list[0:num_people_follow],sleep_delay = 5)
                      session.like_by_users(my_list[0:num_people_follow], amount=num_likes_per_follow)

elif sys.argv[4] == 'no':
                  session = InstaPy(username=insta_username,
                  password=insta_password,
                  page_delay=5,
                  headless_browser=True)

                  with smart_run(session):
                      session.follow_by_list(followlist = my_list[0:num_people_follow],sleep_delay = 5)
