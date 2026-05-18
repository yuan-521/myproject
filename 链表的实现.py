
class Node:
    '节点类:两部分组成，元素区域，指针区域'
    def __init__(self,date,next_Node=None):
        self.date=date
        self.next=next_Node



class SiginleLinkList:
    '单项链表'
    def __init__(self):
        self.head=None  #空的单向链表一开始没有头节点
        self._length=0   #数据个数或者是链表长度为0

    def length(self):
        return self._length  #返回链表的长度

    def is_empty(self):
        return self._length==0  #判断当前链表是否为空



    def add(self,new_date):
        '往头部插入一个新节点'
        node = Node(new_date)
        node.next = self.head #self 表示当前链表
        self.head=node
        self._length +=1


    def append(self,new_date):
        node = Node(new_date)
       # node.next = None  最后一个节点next 默认指向空，可去除
        if self.is_empty():  #原来的链表为空
            self.head=node
        else:         #链表不为空，从头节点依次往下找，直到最后节点
            cur=self.head
            while cur.next:
                cur=cur.next  #cur成为最后一个节点
            cur.next=node
        self._length += 1

    def insert(self,new_date,pos):  #把新的数据插入到指定位置，
        node = Node(new_date)
        if pos <=0:   #插入链表头部
            self.add(new_date)
        elif pos >=self._length:   #pos 越界了,则插入到链表尾部
            self.append(new_date)
        else:  #插入链表中间
             #找到要插入的位置
            cur=self.head
            while pos-1:
                cur=cur.next
                pos-=1
            node.next=cur.next
            cur.next=node
            self._length+=1


    def remove(self,date):
        '删除指定的节点的数据'
        cur=self.head
        pre =None
        while cur:
            if cur.date==date:  #找到了需要删除的节点
                if pre:  #前一个节点
                    pre.next=cur.next  #删除操作：前一个节点的下一个指向当前的下一个
                else:   #要删除的节点就是头节点
                    self.head=cur.next
                self._length-=1
                return True
            else:
             '没有找到，继续往下便利'
            pre = cur
            cur = cur.next
        return False

    def remove_pos(self,pos):
        '删除指定位置的节点'
        if pos <=0:   #删除头节点
            self.head=self.head.next

        elif pos >=self._length:   #pos 越界了,则删除尾节点
            cur = self.head
            pre=None
            while cur.next:
                pre=cur
                cur = cur.next  # cur成为最后一个节点
            pre.next = None        #删除最后一个节点

        else:  #删除链表中间的某个节点

            pre = self.head

            while pos - 1:
                pre = pre.next
                pos -= 1
            cur=pre.next
            pre.next=cur.next
        self._length -= 1
        return True
















    def to_list(self):  #把当前链表转换为列表
        res=[]
        cur=self.head
        while cur:
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
        cur=self.head  #xxxxxxxxxxxxxxxwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
        while cur:  #只要节点还存在，就继续遍历
            if cur.date==date:
                return  True
            cur=cur.next
        return  False



if __name__ == '__main__':
    sll=SiginleLinkList()
    sll.add(11)
    sll.append(44)
    sll.add(89)
    sll.append(78)     #89,11,44,78
    sll.insert(99,2)
    sll.remove(44)
    #print(sll.remove_pos(1))
    print(sll.search(11))
    print(sll.modify(1,1222))
    print(sll.to_list())