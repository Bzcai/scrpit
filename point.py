#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# -*- coding: UTF-8 -*-

import requests
import sys
import random
import lib


mobile = sys.argv[2]
amount = sys.argv[1]
account = lib.getMemberId(mobile)
random = str(random.randint(1,1000000))
url = 'http://user.uat.chunbo.com:88/Points/add/member_id/'+account+'/number/'+amount+'/operation_type/8/voucher_number/'+random
# print(url)
a = requests.get(url)
print(a.text)