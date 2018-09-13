# -*- coding: utf-8 -*-
import urllib2
import json
import pytz
import datetime
#print pytz.all_timezones
localtime = datetime.datetime.now()
localtimeStr=localtime.strftime("%Y-%m-%d %H:%M:%S")
#print localtime
# 2018-04-26 07:50:15.320000

tz = pytz.timezone("UTC")

time = datetime.datetime.now(tz)+datetime.timedelta(minutes=-1)
#datetime.datetime.now()+datetime.timedelta(days=-1)
timeStr=time.strftime("%Y-%m-%d %H:%M:%S")
#print time
#print timeStr
# 2018-04-25 23:50:15.320000+00:00
data = {
    "query": "select count(*) FROM basePayBill where __time>='"+timeStr+"'"
}
headers = {'Content-Type': 'application/json'}
request = urllib2.Request(url='http://172.31.12.101:8082/druid/v2/sql/', headers=headers, data=json.dumps(data))
response = urllib2.urlopen(request)
code=str(response.getcode())
print localtimeStr+"请求Druid 返回状态为："+code
print localtimeStr+"请求Druid 返回结果为："+response.read()