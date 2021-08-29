tests=int(input())
forgot=int(input())
cities=int(input())
dist,visit=[],[]
p,nc,sdist=0,0,0
for i in range(cities):
    dist.append([int(i) for i in input().split()])
    visit.append(0)
for i in range(cities):
        if visit.count(0)==1:
            sdist+=dist[nc][forgot-1]
            sdist+=dist[forgot-1][0]
            break
        p=nc
        minn=1000000
        for index,dis in enumerate(dist[nc]):
                if dis!=0 and dis<minn and visit[index]!=1:
                    minn=dis
                    nc=index
        sdist+=minn
        visit[p]=1
print(sdist)
