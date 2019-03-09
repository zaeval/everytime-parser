"""
Everytime 서비스 파싱 모듈
"""

import requests
from bs4 import BeautifulSoup
import pickle
import datetime

time_table_url = "https://timetable.everytime.kr/ajax/timetable/wizard/getOneTable"
time_table_list_url = "https://timetable.everytime.kr/ajax/timetable/wizard/getPrimaryTableList"
semester_url = "https://timetable.everytime.kr/ajax/timetable/wizard/getSemesters"
root_url = "https://everytime.kr"
friend_url = "https://everytime.kr/ajax/friend/getfriendlist"
DEFAULT_YEAR = 2017

def get_timetable_user_id(ses,friend_token):
    bs = BeautifulSoup(ses.post(root_url+"/find/timetable/table/friend",data={
        'identifier': friend_token,
        'friendInfo': "true"
    }).text,'html.parser')
    name = bs.find("user").get("name")
    names = bs.select('name')
    times = bs.select('time')
    ret=[]
    for idx in range(len(names)):
        ret.append({'name':names[idx].get('value'),'time':[
            {
                'day':time.get('day'),
                'starttime':time.get('starttime'),
                'endtime':time.get('endtime')
            } for time in times[idx].select('data')
        ]});


    return {'name':name,'data':ret}

def login(uid, pwd):
    ses = requests.Session()
    req = ses.post(root_url + "/user/login", data={
        "userid": uid,
        "password": pwd,
    })
    return ses,req

def my_info(ses):
    res = ses.post('https://everytime.kr/my')
    bs = BeautifulSoup(res.text, 'html.parser')
    my_info_keys = ['id', 'name', 'nickname', 'email', 'school']
    my_info = {}
    try:
        for key in range(len(my_info_keys)):
            my_info[my_info_keys[key]] = bs.findAll('em')[key].text
    except Exception:
        return None

    return my_info
def register(id, password, email, name, nickname):
    ses = requests.Session()
    req = ses.post(root_url + '/save/user', data={
        'userid': id,
        'password': password,
        'name': name,
        'nickname': nickname,
        'email': email,
        'campus_id': "62",
        'enter_year': "2018",
        'remote_addr': "",
        'ad_agreement': 0,
        "installer_name": "",
    })
    if BeautifulSoup(req.text,'html.parser').find("response").text == "1":
        print("성공적으로 회원가입을 완료 했습니다.")
    else:
        print("회원가입 실패.")

def send_friend(ses,friend_id=None,file=None):
    if file==None and friend_id!=None:
        req = ses.post(root_url+"/save/friend/request",data={'data':friend_id})
        bs = BeautifulSoup(req.text,'html.parser')
        if bs.find("response").text == '1':
            return "친구요청에 성공했습니다 : " + friend_id
        else:
            return "친구요청에 실패했습니다 : " + friend_id
    elif file!=None:
        with open(file, 'r') as f:
            lines = f.readlines()
            ret = ""
            for friend_id in lines:
                req = ses.post(root_url + "/save/friend/request", data={'data': friend_id.rstrip()})
                bs = BeautifulSoup(req.text, 'html.parser')
                if bs.find("response").text == '1':
                    ret += "친구요청에 성공했습니다 : " + friend_id
                else:
                    ret += "친구요청에 실패했습니다 : " + friend_id
            return ret
    else:
        return "친구요청실패"

def get_friend_list(ses):
    req = ses.post(root_url+"/find/friend/list")
    bs = BeautifulSoup(req.text,'html.parser')
    ret = []
    for tag in bs.select("friend"):
        ret.append({'name':tag.get("name"),'userid':tag.get('userid')})
    return ret

def union_time_table(friend_timetables):
    days = [[],[],[],[],[],[],[]]
    for friend in friend_timetables:
        for times in friend['data']:
            for time in times['time']:
                start_time = float(time['starttime']) / 12
                end_time = float(time['endtime'])/12
                days[int(time['day'])].append((start_time,end_time))

    ret = [[],[],[],[],[],[],[]]
    day_num = 0
    for day in days:
        day.sort(key=lambda time: (time[0],time[1]))
        if(len(day) > 0):
            start = day[0][0]
            end = day[0][1]
        else:
            continue
        for idx in range(1,len(day)):
            after = day[idx]
            a_start = after[0]
            a_end = after[1]

            if end > a_start and a_end > end:
                end = a_end
            if end < a_start:
                ret[day_num].append((start,end))
                start = a_start
                end = a_end
        ret[day_num].append((start, end))
        day_num += 1

    return ret

def empty_time_table(friend_timetables):
    utt = union_time_table(friend_timetables)

    ret = [[],[],[],[],[],[],[]]
    day_num = 0
    for uts in utt:
        start = 0
        end = 0
        for time in uts:
            a_start = time[0]
            a_end = time[1]
            end = a_start
            ret[day_num].append((start,end))
            start = a_end
        ret[day_num].append((start,24))

        day_num += 1

    return ret

