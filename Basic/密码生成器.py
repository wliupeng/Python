#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
def mima(x):   #密码生成器
	from random import choice
	mima=[]
	mima2=[]
	for i in range(1,x):
		for y in range(1,13):
			a1=choice('abcdefghijklmnopqrstuvwxyzABCDEFGIHJKLMNOPQRSTUVWXYZ01234567890~!@#$%^&*()')
			mima.append(a1)
		mima2.append(''.join(mima))
		mima=[]
	return mima2
if __name__ == '__main__':
	print(mima(5))