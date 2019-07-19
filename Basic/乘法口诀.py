for i in range(1,11):
	a=i
	b=1
	while b<=a:
		if b!=a:
			s=a*b
			print('%2d*%-2d=%2d'%(a,b,s),sep=' ',end=' ')
			b+=1
		if b==a:
			s=a*b
			print('%2d*%2d=%2d'%(a,b,s))
			b+=1
