# '''         8            '''


## thre is no define which condition work firstly
# some time both thread work simultanously


# from threading import Thread, current_thread

# class Flight:
#     def __init__(self, available_seat):
#         self.available_seat = available_seat

#     def reserve(self, need_seat):
#         print("Available Seat :", self.available_seat)

#         if(self.available_seat >= need_seat):
#             name = current_thread().name
#             print(f'{need_seat} seat is alloted for {name}')
#             self.available_seat -= need_seat

#         else:
#             print('Sorry! All seats has Alloted')

# f = Flight(1)

# s1 = Thread(target=f.reserve, args=(1,), name="Vaibhav")
# s2 = Thread(target=f.reserve, args=(1,), name="Rahul")

# s1.start()
# s2.start()

'''-----------------------------------------------------------------------'''


