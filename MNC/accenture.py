class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def UncommonNodes(list1,list2):
    if list1==None:
        return None
        
    l1,l2=[],[]
    p,q=list1,list2
    while(p!=None):
        l1.append(p.data)
        p=p.next
    while(q!=None):
        l2.append(q.data)
        q=q.next
    if l1==l2:
        return None
    for i in l1:
        if i in l2:
            l1.remove(i)
    
    for i in range(len(l1)):
        if i==0:
            list3=Node(l1[i])
            r=list3
        else:
            r.next=Node(l1[i])
            r=r.next
    return list3
    
        
        

l1=[14,11,2,10,3]
l2=[11,7,10]
l1=Node(14)
l1.next=Node(11)
l1.next.next=Node(2)
l1.next.next.next=Node(10)
l1.next.next.next.next=Node(3)
        
l2=Node(11)
l2.next=Node(7)
l2.next.next=Node(10)
UncommonNodes(l1,l2)
    
    
    
