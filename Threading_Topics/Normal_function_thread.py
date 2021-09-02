####'''   1   '''




# import threading

'''------------------------------------------'''
# current thread object name or current thread
'''-------------------------------------------'''

# print(threading.current_thread().name)

'''----------------------------------------------'''

# t = threading.current_thread().getName()

# print(t)

'''------------------------------------------'''
# from threading import Thread
'''-------------------------------------------'''
# thread without class and argument

# def disp():
#     print("Thread running")

# t = Thread(target=disp)

# t.start()

'''------------------------------------------------'''
# one argument and use tuple method

# def disp(a):
#     print("thread running :", a)

# t = Thread(target=disp, args=(10,))
#                                         # is an tuple should be use "," after int or every argument
# t.start()

'''-------------------------------------------------'''
# using two argument

# def disp(a,b):
#     print("thread running :", a,b)

# t = Thread(target=disp, args=(10,20))

# t.start()

'''-----------------------------------------------------'''
# thread run multiple times using for loop

# def disp(a,b):
#     print("thread running :", a,b)

# for i in range(5):
#     t = Thread(target=disp, args=(10,20))

#     t.start()

'''---------------------------------------------------------'''

# def disp(a,b):
#     print("thread running :", a,b)

# for i in range(5):
#     t = Thread(target=disp, args=(10,20))

# t.start()

'''-----------------------------------------------------------'''
# write any python program there run own main thread

# def disp():
#     print("child thread")

# t = Thread(target=disp)

# t.start()

# for i in range(5):
#     print("main thread")

'''-------------------------------------------------------------'''
# using for loop both side to see both thread are work differently
# they are not depend to each other but both are same program part

# using thread 

# def disp():
#     for i in range(5):
#         print("child thread")

# t = Thread(target=disp)

# t.start()

# for i in range(5):
#     print("main thread")
