with open('input1.txt','r') as file:
#with open('input1-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

for line in lines:
    for i in range(9,0,-1):
       if str(i) in line:
           
