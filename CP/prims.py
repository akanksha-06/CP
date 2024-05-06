import heapq
def prims(graph):
    al={v:[] for v in graph['vertices']}
    mst=[]
    for edge in graph['edges']:
        al[edge[0]].append((edge[1],edge[2]))
        al[edge[1]].append((edge[0],edge[2]))
    start="a"
    visited=set()
    visited.add(start)
    q=[(weight,start,dest) for dest,weight in al[start]]
    while q :
        w,s,d=heapq.heappop(q)
        if d not in visited:
            visited.add(d)
            mst.append((w,s,d))
            for n,w in al[d]:
                if n not in visited:
                    heapq.heappush(q,(w,d,n))
    print(mst)
    mindist=0
    for e in mst:
        mindist=mindist+e[0]
    print(mindist)
    

graph={
    "vertices":['a','b','c','d','e'],
    "edges":[('a','b',2),('b','d',4),('d','e',5),('c','e',1),('a','c',3),('c','d',6)]
}
prims(graph)
