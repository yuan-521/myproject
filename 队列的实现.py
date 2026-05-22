#先进先出，从某一端操作插入，另一端删除
class MyQueu(object):   #栈
    def __init__(self,maxlen=0):
        self.maxlen=maxlen
        self.items=[]

    def is_empty(self):
        return  len(self.items)==0
    def size(self):
        return len(self.items)
    def push(self,new_date):    #把元素添加到队列中
        if self.maxlen>0 and len(self.items)==self.maxlen:
            raise Exception("队列的元素数量已经达到最大值")
        self.items.insert(0,new_date)

    def pop(self):
        "删除出一个元素"
        return self.items.pop()




if __name__ =='__main__':
    s=MyQueu(maxlen=10)
    print(s.is_empty())
    s.push("hello")
    s.push("123")
    s.push("时代少年团")
    print(s.size(),s.is_empty())
    print(s.pop())     #删除hello

    print(s.size(),s.is_empty())


    from  queue import Queue
    queue=Queue()
    















































