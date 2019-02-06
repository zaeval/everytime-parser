import sys
sys.path.append("..")

import everytime

ses,res = everytime.login("YOUR_ID","YOUR_PASSWORD")
print(everytime.send_friend(ses,file='alias.txt'))
