from instapy import InstaPy
from instapy import smart_run
import sys



# login credentials

insta_username = sys.argv[1]
insta_password = sys.argv[2]


# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

num_people_unfollow = int(sys.argv[3])
with smart_run(session):
    mylist = session.grab_following(username=sys.argv[1], amount="full", live_match=True, store_locally=True)
    mylist = mylist[-num_people_unfollow:]
    mylist.reverse()
    session.unfollow_users(amount =num_people_unfollow, custom_list_enabled = True,custom_list = mylist)
