


class Node:
    '节点类:两部分组成，元素区域，指针区域'
    def __init__(self,date,   prev_node=None ,next_Node=None):
        self.date=date
        self.next=next_Node #链接到后一个节点
        self.prev=None  #链接到前一个节点


class DoubleLinkList:
    '双向链表'

    def __init__(self):
        self.head=None  #空的单向链表一开始没有头节点
        self._length=0   #数据个数或者是链表长度为0



    def length(self):
        return self._length  #返回链表的长度

    def is_empty(self):
        return self._length==0  #判断当前链表是否为空



    def add(self,new_date):
        '往头部插入一个新节点'
        node=Node(new_date)
        if  self.is_empty():
            self.head=node
        else:
            self.head.prev=node    # 链表中原来的head 节点的prev指向新建的节点node
            node.next=self.head     #插入的节点指向原来的头节点
            self.head=node      #把新建的node节点作为头节点



        self._length +=1


    def append(self,new_date):
        node = Node(new_date)
       # node.next = None  最后一个节点next 默认指向空，可去除
        if self.is_empty():  #原来的链表为空
            self.add(new_date)
        else:         #链表不为空，从头节点依次往下找，直到最后节点
            cur=self.head
            while cur.next !=self.head:
                cur=cur.next  #cur成为最后一个节点
            cur.next=node    #尾节点指向插入的真正尾节点
            node.next=self.head
        self._length += 1

    def insert(self,new_date,pos):  #把新的数据插入到指定链表的位置，
        node = Node(new_date)
        if pos <=0:   #插入链表头部
            self.add(new_date)
        elif pos >=self._length:   #pos 越界了,则插入到链表尾部
            self.append(new_date)
        else:  #插入链表中间
             #找到要插入的位置
            node=Node(new_date)
            cur=self.head
            while pos-1:
                cur=cur.next
                pos-=1
            node.next=cur.next    #原来是cur~cur.next.变成cur     node~cur.next
            cur.next=node
            self._length+=1


    def remove(self,date):
        '删除指定的节点的数据'
        cur=self.head
        pre =None
        flag=True                     #第一次循环的标记。让循环链表只遍历一次
        while cur and flag: #如果当前节点存在并且
            if cur.next==self.head:   #循环遍历至尾节点，第一次循环完成
                flag=False    #不满足83行，终止循环
            if cur.date==date:                       #判断删除的数据是不是当前节点的数据
                if pre:                              #如果有前一个节点
                    pre.next=cur.next         #删除操作：前一个节点的下一个指向当前的下一个
                else:                               #要删除的节点就是头节点
                    #先找到尾节点
                    last_node=self.head
                    while last_node.next!=self.head:
                        last_node.head=last_node.next      #找到尾节点
                    last_node.next=self.head.next
                    self.head=cur.next

                self._length-=1
                return True
            else:
             '没有找到，继续往下便利'
            pre = cur
            cur = cur.next
        return False





    def to_list(self):  #把当前链表转换为列表
        res=[]
        cur=self.head
        flags=True
        while cur and flags:
            if cur.next==self.head:
                flags=False
            res.append(cur.date)
            cur=cur.next
        return res


    def modify(self,pos,new_date):
        if 0<=pos<self._length:
            cur =self.head
            while pos:
                cur=cur.next
                pos-=1
            cur.date=new_date
        else:
            print("输入的下标有误！")


    def search(self,date):
        if self.is_empty():
            return False
        flags=True
        cur=self.head  #xxxxxxxxxxxxxxxwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
        while cur and flags:  #只要节点还存在，就继续遍历
            if cur.next==self.head:
                flags=False
            if cur.date==date:     #如果节点的值等于要判断的值
                return  True
            cur=cur.next
        return  False



if __name__ == '__main__':
    sll=DoubleLinkList()
    sll.add(11)
    sll.append(44)
    sll.append(78)
    sll.add(89)     #89,11,44,78

    print(sll.to_list())
    sll.insert(99,2)
    #print(sll.remove_pos(1))
    print(sll.search(33))
    print(sll.to_list())
