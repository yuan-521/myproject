
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

    def to_list(self):  #把当前链表转换为列表
        res=[]
        cur=self.head
        while cur:
            res.append(cur.date)
            cur=cur.next
        return res


if __name__ == '__main__':
    sll=SiginleLinkList()
    sll.add(11)
    sll.append(44)
    sll.add(89)
    print(sll.to_list())