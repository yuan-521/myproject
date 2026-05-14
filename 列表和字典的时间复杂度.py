
import timeit

def list_append():
    lst = []
    for i in range(10001):
        lst.append(i)

def list_insert_end():
    lst = []
    for i in range(10001):
        lst.insert(-1,i)

def list_insert_head():
    lst = []
    for i in range(10001):
        lst.insert(0,i)

def list_extend():
     lst = []
     for i in range(10001):
         lst.extend([i])




if __name__=='__main__':
    t=timeit.Timer('list_append()',globals={'list_append':list_append})
    print(f"{list_append.__name__}函数运行时间为：{t.timeit(1000)}秒")

