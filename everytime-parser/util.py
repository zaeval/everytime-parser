import datetime
import requests


def int2datetime(li):
    # print(time['day'],datetime.timedelta(hours=start_time),datetime.timedelta(hours=end_time))
    day_alias=['MON','TUE',"WED","THU","FRI","SAT","SUN"]
    ret = []
    for idx, day in enumerate(li):
        dic = {}
        dic["day"] = day_alias[idx]
        dic["time"] = []
        for time in day:
            dic["time"].append(
                {
                    'start_time' : str(datetime.timedelta(hours=time[0])),
                    'end_time' : str(datetime.timedelta(hours=time[1])),
                }
            )

        ret.append(dic)

    return ret