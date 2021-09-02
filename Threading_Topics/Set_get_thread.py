# '''     2     '''


# from threading import Thread, current_thread

# using current_thread function it shows currently using thread 
# this function return current thread object

# def disp():
#     print("child thread :", current_thread())

# t = Thread(target=disp)

# t.start()

# print("main thread :", current_thread())

'''--------------------------------------------------------------------'''
# using function find the name of thread

# def disp():
#     print("child thread :", current_thread().getName())

# t1 = Thread(target=disp)
# t2 = Thread(target=disp)

# t1.start()
# t2.start()

# print("main thread :", current_thread().getName())

'''-------------------------------------------------------------------------------'''
# using set we set the name of the thread

# def disp():
#     print("Default Thread :", current_thread().getName())
#     current_thread().setName('spoiler thread')
    
#     print("New Thread name :", current_thread().getName())

# t = Thread(target=disp)

# t.start()

# print("Default Thread Name :", current_thread().getName())
# current_thread().setName("server spoiler thread")

# print("New Main thread Name :", current_thread().getName())

'''-------------------------------------------------------------------------'''
# another method to get and set thread name

# def disp():
#     print("Default Thread :", current_thread().name)
#     current_thread().name = "setting"
    
#     print("New Thread name :", current_thread().name)

# t = Thread(target=disp)

# t.start()

# print("Default Thread Name :", current_thread().name)
# current_thread().name = "pro thread"

# print("New Main thread Name :", current_thread().name)

'''----------------------------------------------------------------------------'''

# from threading import Thread

'''--------------------------------------------------------------------------------'''
# no need to be write a function you use pass it will give you 
# a name of thread

# def disp():
#     pass

# t = Thread(target=disp())
# print(t.getName())
# t.setName('doc type')
# print(t.getName())

'''-----------------------------------------------------------------------'''
# another method set and get

# def disp():
#     pass

# t = Thread(target=disp)
# print("Default", t.name)
# t.name = "fly"
# print("New", t.name)

'''------------------------------------------------------------------------'''
# just add parameter and you can set the name


# def disp():
#     pass

# t = Thread(target=disp, name='Toy')

# print(t.name)


