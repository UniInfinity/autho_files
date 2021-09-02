# '''      7        '''

# Two task using two thread

# from threading import Thread

# class Hotel:
    
#     def __init__(self, t):
#         self.t = t

#     def food(self):
#         for i in range(1,6):
#             print(self.t, i)

# h1 = Hotel("Take Order from Table")
# h2 = Hotel("Serve Order to Table")

# s1 = Thread(target=h1.food)
# s2 = Thread(target=h2.food)

# s1.start()
# s2.start()