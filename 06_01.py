with open('input6.txt','r') as file:
#with open('input6-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]


sumgrid=[]
operline=[]
for line in lines:
    myline=[]
    if '*' in line:
       for i in line.split():
          operline.append(i)
    else:
        for i in line.split():
           myline.append(int(i))
        sumgrid.append(myline)

bigsum=0
for i,oper in enumerate(operline):
    if oper == '+':
        smallsum=0
        for row in sumgrid:
              smallsum+=row[i]
    else:
        smallsum=1
        for row in sumgrid:
              smallsum*=row[i]
    bigsum+=smallsum
    
print(bigsum)
