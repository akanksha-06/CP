class Node:
    def __init__(self,data):
        self.lc=None
        self.rc=None
        self.data=data
        self.hd=0
def vertical_order(root):
    vertical_map={}
    q=[(root,0)]
    while q:
        node,hd=q.pop(0)
        if hd not in vertical_map:
            vertical_map[hd]=[]
        vertical_map[hd].append(node.data)
        if node.lc:
            q.append((node.lc,hd-1))
        if node.rc:
            q.append((node.rc,hd+1))
    print("vertical order traversal")
    for hd in vertical_map:
        print(vertical_map[hd],end=",")
def level_order(root):
    vertical_map={}
    q=[(root,0)]
    while q:
        node,hd=q.pop(0)
        if hd not in vertical_map:
            vertical_map[hd]=[]
        vertical_map[hd].append(node.data)
        if node.lc:
            q.append((node.lc,hd+1))
        if node.rc:
            q.append((node.rc,hd+1))
    print("Level order traversal")
    for hd in vertical_map:
        print(vertical_map[hd],end=",")
def rlevel_order(root,order="BT"):
    vertical_map={}
    q=[(root,0)]
    while q:
        node,hd=q.pop(0)
        if hd not in vertical_map:
            vertical_map[hd]=[]
        vertical_map[hd].append(node.data)
        if node.lc:
            q.append((node.lc,hd+1))
        if node.rc:
            q.append((node.rc,hd+1))
    if order=="TB":
        print("\nlevel order traversal :")
        for hd in vertical_map:
            print(vertical_map[hd],end=",")
    elif order=="BT":
        print("\nrlevel order traversal :")
        for hd in sorted(vertical_map,reverse=True):
            print(vertical_map[hd],end=",")
        
    
root=Node('A')
root.lc=Node('B')
root.rc=Node('C')
root.lc.lc=Node('D')
root.lc.rc=Node('E')
root.rc.lc=Node('F')
root.rc.rc=Node('G')
vertical_order(root)
level_order(root)
rlevel_order(root)
