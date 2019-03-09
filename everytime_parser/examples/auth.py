import sys
sys.path.append("..")

import everytime
# TODO: register to everytime
everytime.register("everytest5","password",'everytest5@naver.com',"everyname5","everynick5")

# TODO: login
ses,res = everytime.login("everytest4", "password")
print(ses.cookies.items()[0])
ses.cookies.set('etsid','s%3Ai_y0wEW4D08tR0aVq1r23ihneXYs5mmI.mRQJ0aNa5G81GoM%2BxSkZq8sokW0q1d6WFRkRL%2FidBik')

print(everytime.my_info(ses))