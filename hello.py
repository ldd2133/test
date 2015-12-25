#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
def list(len,bc):
	for num in range(0,int(len/bc)):
		f = open('E:\py/py_%d.txt'%num,'w')
		for i in range(num*bc,(num)*bc+bc,10000):	
			b_list = range(i+1,i+10001)
			blist_webld = random.sample(b_list,10000)
			f.write(sorted(blist_webld))
		f.close()

	
a = 100000000  #数值
b = 1000000   #步长
list(a,b)
