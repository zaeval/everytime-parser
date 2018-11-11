import requests

ROOT_URL = "https://everytime.kr"
ses = requests.Session()
for i in range(11, 20):
    temp = "kookmin"
    number = str(i)
    uid = temp + number
    pwd = "password"
    name = uid
    nickname = uid
    email = "aazaf" + str(i) + "@naver.com"
    req = ses.post(ROOT_URL + '/save/user', data={
        'userid': uid,
        'password': pwd,
        'name': name,
        'nickname': nickname,
        'email': email,
        'campus_id': "62",
        'enter_year': "2018",
        'remote_addr': "",
        'ad_agreement': 0,
        "installer_name": "",
    })

    print(req.text)
