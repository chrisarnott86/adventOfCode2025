with open('input1.txt','r') as file:
#with open('input1-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]


pointer=50
zeros=0
for line in lines:
    rot=line[0]
    value=int(line[1:])
    
    if rot=='L':
       pointer = (pointer - value)%100
    else:
       pointer = (pointer + value)%100
    
    if pointer == 0:
       zeros+=1

print(zeros)
