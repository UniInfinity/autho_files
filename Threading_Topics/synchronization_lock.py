# '''      9          ''''


from threading import Thread, current_thread, Lock

class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.l = Lock()

    def reserve(self, need_seat):
        print("Available Seat :", self.available_seat)
        self.l.acquire()

        if(self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat -= need_seat

        else:
            print('Sorry! All seats has Alloted')

        self.l.release()


f = Flight(3)

s1 = Thread(target=f.reserve, args=(2,), name="Vaibhav")
s2 = Thread(target=f.reserve, args=(1,), name="Rahul")
s3 = Thread(target=f.reserve, args=(1,), name="ketan")

s1.start()
s2.start()
s3.start()


