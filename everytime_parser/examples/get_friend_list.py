import sys
sys.path.append("..")

import everytime

friend_timetables = []
ses,res = everytime.login("YOUR_ID","YOUR_PASSWORD")

friends = everytime.get_friend_list(ses)
for friend in friends:
    temp = everytime.get_timetable_user_id(ses, friend["userid"])
    friend_timetables.append(temp)
union = everytime.union_time_table(friend_timetables)
empty = everytime.empty_time_table(friend_timetables)

print(union)
print(empty)

import util

print(util.int2datetime(empty))
