'''
import asyncio

async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")
    
# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
'''
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)


list1 = ['Google', 'Runoob', 'Taobao']
# list_pop=list1.pop(1)
list_pop=list1.pop()
print ("删除的项为 :", list_pop)
print ("列表现在为 : ", list1)