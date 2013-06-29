import random

#    /_
#   | \
def gr(x, y,n):
    ur = []
    r = [] 
    rd=[]
    d = []
    for  i in range(n):
        ur.append((x-i , y+i,))
        r.append((x, y+i,))
        rd.append((x+i, y+i,))
        d.append((x+i, y,))
    yield ur  #up-right
    yield r   #right 
    yield rd  #right down
    yield d   #down

def allNCombination(a,n):
    validCoordinate =  lambda  xy : xy < len(a) and xy >=0 
    validRange =  lambda  r : len(filter (validCoordinate, r)) == 2
    value = lambda p: a[p[0]][p[1]]
    for y in range(len(a)):
       for x in range(len(a[y])): 
          for r in gr(x, y, n):
             if len(filter(validRange, r)) == n:
                 yield map(value,r)
M=10
nn=3
#for test
c =  [ [ int(random.random() * 1031 * random.choice([-1,1])) for x in range(M)] for y in range(M) ] 
for cc in c :
    print cc
c=[r for r in allNCombination(c, nn)]

for cc in c :
    print cc
op = lambda s:[reduce (lambda x,y: x*y,  s, 1),s]
c=map(op, c)
cmp = lambda k: k[0]
print max(c , key=cmp)


