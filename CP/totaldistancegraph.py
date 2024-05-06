edgelist=[("a","b",2),("b","d",4),("d","e",5),("d","c",6),("e","c",1),("a","c",3)]
tot=0
for edge in edgelist:
    tot=tot+edge[2]
print("total distance = ",tot)
vset=set()
for edge in edgelist:
    vset.add(edge[0])
    vset.add(edge[1])
#print(vset)
al={v:[] for v in vset}
for edge in edgelist:
    al[edge[0]].append((edge[1],edge[2]))
    al[edge[1]].append((edge[0],edge[2]))
print("adjacancy list is = ",al)
        
