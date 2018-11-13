import sys
sys.path.append("..")

import everytime
# TODO: register to everytime
everytime.register("everytest4","password",'everytest4@naver.com',"everyname4","everynick4")

# TODO: login
ses = everytime.login("everytest4", "password")

