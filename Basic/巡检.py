#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import time
from telnetlib import Telnet
from datetime import datetime
ip =['192.168.100.10','192.168.100.11']
now=datetime.now()
year=now.year
month=now.month
day=now.day
hour=now.hour
minute=now.minute
filename='/home/python/xunjian/xunjian_'+str(year)+'_'+str(month)+'_'+str(day)+'_'+str(hour)+'_'+str(minute)+'.txt'
xunjian=open(filename,'a')
for x in ip:
	tn = Telnet(x,23)
	tn.write(b'cisco\n')
	time.sleep(0.1)
	tn.write(b'cisco\n')
	time.sleep(0.1)
	tn.write(b'show ip interface brief\n')
	time.sleep(0.1)
	tn.write(b' ')
	time.sleep(0.1)
	xs = (tn.read_very_eager()).decode('utf8')
	print('='*80,file=xunjian)
	print(xs,file=xunjian)
	print(x+'is ok',file=xunjian)
	print('='*80,file=xunjian)
	print(x+'    is ok')
	print('='*30)