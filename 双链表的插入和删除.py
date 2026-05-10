class LNode:
    def __init__(self, data=None):#创建单个节点，给其中初始化赋值
        self.data = data
        self.next = None
        self.prior = None
    def __str__(self):#
        return str(self.data)

class LinkList:
    def __init__(self):# 初始化链表
        self.head = LNode(None)
    def __iter__(self):   #遍历整个链表
        p = self.head
        while p is not None:
            yield p
            p = p.next
    def list_insert_dul(self, i, e):  #插入
        for idx, p in enumerate(self):
            if idx == i:
                s = LNode(e)
                s.prior = p
                s.next = p.next
                p.next = s
                if s.next is not None:
                    s.next.prior = s
                return
        raise Exception('位置不合法')
    def list_delete_dul(self, i):   #删除
        for idx, p in enumerate(self):
            if idx == i:
                p.prior.next = p.next
                if p.next is not None:
                    p.next.prior = p.prior
                return
        raise Exception('位置不合法')
    def __str__(self):    #打印链表格式
        output = ''
        for idx, item in enumerate(self):
            if idx > 0:
                output += ' <--> ' + str(item.data)
        return output