from subprocess import call
while 1:
    y1=input('y = ')
    y='        y= '+y1+'\n'
    f=open('.\Graph.py')
    q=f.readlines()
    #print(q[44])
    q[44]=y
    f.close()
    f=open('.\Graph.py','w')
    f.writelines(q)
    f.close()
    c2=call("python Graph.py",shell=1)
