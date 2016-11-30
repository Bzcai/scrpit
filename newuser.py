#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# -*- coding: UTF-8 -*-

import requests
import sys

if sys.argv[1] is None:
    mobile = 13800138000
else:
    mobile = sys.argv[1]
#print(mobile)
url = 'http://api.uat.chunbo.com:90/Sms/setVerifyApi/mobile/'+mobile+'/verify/1234'
#print(url)
a = requests.get(url)
#print(a.url)
print(a.text)