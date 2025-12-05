from math import floor
#with open('input1.txt','r') as file:
with open('input1-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]


pointer=50
zeros=0
for line in lines:
    rot=line[0]
    value=int(line[1:])
    
    wraps = 0
    
    if rot=='L':
       pointer = (pointer - value)%100
       wraps = (pointer - value)//100
    else:
       pointer = (pointer + value)%100
       wraps = (pointer + value)//100
    
    if pointer == 0:
       zeros+=1
    
    print(wraps)
    zeros+=abs(wraps)
#    print(pointer)

print(zeros)
