with open('input2.txt','r') as file:
#with open('input2-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

badsum=0
for line in lines:
    for idrange in line.split(','):
        for i in range(int(idrange.split('-')[0]),int(idrange.split('-')[1])+1):
            if len(str(i))%2==0:
                if str(i)[:len(str(i))//2]==str(i)[len(str(i))//2:]:
                    badsum+=i
                    
print(badsum)
