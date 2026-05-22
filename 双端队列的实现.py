# 从两端任意的插入和删除
class DoubleMyQueu(object):  # 栈
    def __init__(self, maxlen=0):
        self.maxlen = maxlen
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def add(self, new_date):  # 把元素从右侧添加到双端队列中
        if self.maxlen>0 and self.maxlen==self.size():
            raise Exception("队列的元素数量以达到最大值")
        self.items.append(new_date)


    def add_left(self, new_date):  #把元素从左侧添加到双端队列中
        if self.maxlen > 0 and self.maxlen == self.size():
            raise Exception("队列的元素数量以达到最大值")
        self.items.insert(0,new_date)

    def pop(self):
        "从右侧删除出一个元素"
        return self.items.pop()
    def pop_left(self):
        "从左侧删除元素"
        return  self.items.pop(0)

    def display (self):
        print(self.items)

if __name__ == '__main__':
    s = DoubleMyQueu(maxlen=10)

    s.add("hello")
    s.add("123")
    s.add("时代少年团")
    print(s.size(), s.is_empty())
    #print(s.display())
    s.display()
    s.add_left("789")
    s.add_left("654")
    s.display()
    print(s.pop())
    print(s.size(), s.is_empty())

    from queue import Queue

    queue = Queue()
















































