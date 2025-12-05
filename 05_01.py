#with open('input5.txt','r') as file:
with open('input5-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]


rangeset=set()
mode="ranges"
bad=0
for line in lines:
    if not line:
        mode="ids"
    if mode=="ranges":
        start=int(line.split('-')[0])
        end=int(line.split('-')[1])
        for i in range(start,end+1):
            rangeset.add(i)
    else:
        if line:
            test=int(line)
            if test not in rangeset:
                bad+=1
print(bad)
