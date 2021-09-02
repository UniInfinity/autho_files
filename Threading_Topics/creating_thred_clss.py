# '''    3     '''


# from threading import Thread

'''------------------------------------------'''
# using class to create a thread 
# inherite the thread in child class

# class Mysteric(Thread):
#     pass

# t = Mysteric()
# print(t.name)

'''------------------------------------------------'''
# run method work when you start that method using start method
# run method automatic call when you start thread method

# class Mysteric(Thread):
#     def run(self):
#         for i in range(5):
#             print("child Method")

# t = Mysteric()
# t.start()

# for i in range(5):
#     print("main thread")

'''-------------------------------------------------------'''
# join method using this method at a time one thread will be
# executed then another thread executed
# after this method first thread completely executed then 
# threads executed


# class Mysteric(Thread):
#     def run(self):
#         for i in range(5):
#             print("child Method")

# t = Mysteric()
# t.start()
# t.join()

# for i in range(5):
#     print("main thread")

'''----------------------------------------------------------------'''
