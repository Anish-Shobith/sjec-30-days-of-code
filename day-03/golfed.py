e=list(map(int,input().split()));[print(a,end=' ')for a in [x for x in e[1:]]if a>sum([x for x in e[1:]])/e[0]]
