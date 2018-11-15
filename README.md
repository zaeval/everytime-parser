# everytime-parser
everytime-parser served by zaeval.

It is using for nonprofit.

![](https://img.shields.io/badge/pip-v0.0.2-blue.svg)
![](https://img.shields.io/github/license/mashape/apistatus.svg)
![](https://img.shields.io/badge/require-requests%20%7C%20bs4-orange.svg)
![](https://img.shields.io/badge/author-zaeval-red.svg)

## HOW 2 INSTALL!
```
pip install everytime-parser
```
or
```
pip3 install everytime-parser
```
or

download the .zip file from top of this page (click the clone button)

## Auth

and then, we need auth.

everytime cannot allowed api to anyone.

in, this library serve login function

```python
import everytime
everytime.login("YOUR_EVERYTIME_UID","YOUR_EVERYTIME_PASSWORD")
```

and this function return session of your user information. So, if you want call another function.

you should save this information into the variable. like this,

```python
import everytime
ses = everytime.login("YOUR_EVERYTIME_UID","YOUR_EVERYTIME_PASSWORD")
```

## Friend

It just served three functions, send request to be friend, get my friend_list 
and get friend's timetable. few month ago, friend's timetable can got with no-auth. but it changed.

first, Introduce send_friend function

```python
import everytime
everytime.send_friend(ses,friend_id="YOUR_FRIEND_ID")
```

if you are success, it return
```
"친구요청에 성공했습니다 : YOUR_FRIEND_ID" 
```

else if you are fail, it return
```
"친구요청에 실패했습니다 : YOUR_FRIEND_ID" 
```

and this function can read file and batched-sending like this,
```python
import everytime
everytime.send_friend(ses,file="TEXT_FILE_PATH")
```

It required notation, with new line split.
```
YOUR_FRIEND_ID_1
YOUR_FRIEND_ID_2
YOUR_FRIEND_ID_3
YOUR_FRIEND_ID_4
        :
        :
```

second, we can get my-friend list. like this,
```python
import everytime
friends = everytime.get_friend_list(ses)
```

and then, we can get friend's time table, too.
```python
friend_timetables = []
for friend in friends:
    temp = everytime.get_timetable_user_id(ses, friend["userid"])
    friend_timetables.append(temp)
```
like this.

## Some Utils

and It served some util function to you.

 - union friend's timetable.
 - find empty friend's timetable(reverse union)
 - change format to see easier
 
## Examples

 - [auth.py](https://github.com/zaeval/everytime-parser/blob/master/everytime-parser/examples/auth.py)
 - [get_friend_list.py](https://github.com/zaeval/everytime-parser/blob/master/everytime-parser/examples/get_friend_list.py)
 - [send_friend.py](https://github.com/zaeval/everytime-parser/blob/master/everytime-parser/examples/send_friend.py)

