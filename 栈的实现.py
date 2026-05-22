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
        if self.maxlen>0 and len(self.items)==self.maxlen:
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
            return self.items[self.size()-1]#[10,20,30]self.size() 返回3；self.size()-1 返回self.items[] 取出30


if __name__ =='__main__':
    s=Stack(maxlen=10)
    print(s.is_empty())
    s.push("hello")
    s.push("123")
    s.push("时代少年团")
    print(s.size(),s.is_empty())
    print(s.pop())     #删除栈顶即最后一个元素
    print((s.peek()))
    print(s.size(),s.is_empty())
