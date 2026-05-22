#先进后出，从某一端操作插入和删除
class Stack(object):   #栈
    def __init__(self,maxlen=0):
        self.maxlen=maxlen
        self.items=[]

    def is_empty(self):
        return  len(self.items)==0
    def size(self):
        return len(self.items)
    def push(self,new_date):    #把元素放入栈，第五行
        if len(self.items)==self.maxlen:
            raise Exception("栈的元素数量已经达到最大值")
        self.items.append(new_date)

    def pop(self):
        "弹出一个元素"
        return self.items.pop()
    def peek(self):
        "返回栈顶元素，不会删除"
        if self.is_empty():
            return  None
        else:
            return self.items[self.size()-1]