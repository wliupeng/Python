#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
def ip(x):   #生成IP地址函数
	from random import randint
	iplist=[]
	for i in range(1,x):
		a=randint(1,255)
		b=randint(1,255)
		c=randint(1,255)
		d=randint(1,255)
		ip=str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)
		iplist.append(ip)
	return iplist
if __name__ == '__main__':
	print(ip(6))