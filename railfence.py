str = input("Please put in the thing to be decoded: ")
rails = int(input("please put in the number of rails: "))
counter = 0
lent = len(str)
zones = len(str)//(rails*2-2)
remain = len(str)%(rails*2-2)
split = []
for x in range(rails):
    split.append(str[0:zones*(1+bool(x!=0 and x!=rails-1))+bool(remain)])
    str=str[zones*(1+bool(x!=0 and x!=rails-1))+bool(remain):]
    remain-=bool(remain)
output = ""
fow = True
for x in range(lent):
    output+=split[counter][0]
    split[counter] = split[counter][1:]
    counter+=fow*2-1
    if counter == rails-1:
        fow=False
    elif counter ==0:
        fow=True
print(output)