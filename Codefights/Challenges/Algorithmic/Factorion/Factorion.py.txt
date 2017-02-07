import string as g;A=g.ascii_uppercase+g.ascii_lowercase+g.digits+'-_';R=dict((c,i)for(i,c)in enumerate(A));B=len(A)
def d(s):
	n=0;sLength=len(s)
	for c in s:n=n*B+R[c]
	return n
def Factorion(b):
	c={'b':['BQq','zUo2ovQYV-v_Ar'],'i':['DjMX01rIJeKanfimLi','aNd_Vd-QT7nW9oFqAnJ','Zv2irhzFaQ27jXRmyxtX','ZxfKeKloEffitcUEwpLa'],'O':['MFRdAa'],'X':['P7cl3ivGOZO6'],'Y':['B5','B6'],'R':['J4R','Jz9mYvj9','Jz9mY5lL'],'J':['KFC'],'Q':['mDztmv5'],'E':['H'],'K':['CR','J6J'],'g':['2Lajvq3Rdn2jY1zmqh','2Lajvq3Rdn2jY1zmqi'],'L':['a','w','J4Y'],'a':['CN0_c3ebhMN','CN0_c3ebhMO'],'l':['DO384sERyWju6Invv9CpG_56'],'j':['Wh'],'e':['BzmYOtD73l-MsnZiaT'],'c':['CQ'],'m':['BGYvhvVCZyLdFErz13z5DqxZ'],'P':['Wh','Wi'],'N':['e9Ewv'],'G':['Z','a'],'F':['x'],'V':['Z'],'k':['DeHWg3kSG_ugauqAz5Uz_k']};f={}
	for k in c:p=d(k);v = [d(l) for l in c[k]];f[p] = v
	z=[1,2];return str(z) if b not in f else str(z+f[b])