class fibi():
    n = int(raw_input("enter number:"))
    print 0,1,
    j = 0;k = 1
    for i in range(n-2):
	m = j+k;j = k;k = m
	print m,
	
