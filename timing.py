class Time:
    def __init__(self , h , m):
        self.h = h
        self.m = m
    
    def show(self):
        print(self.h , ":" , self.m)

    def second_to_time(sec):
        h = sec // 3600
        m = (sec % 3600) // 60
        return Time(h , m)
    
    def time_to_sec(self):
        return (self.h * 3600) + (self.m * 60)
    
    def sum(self , time):
        result = ((self.h * 60) + self.m) + ((time.h * 60) + time.m)
        new_h = result // 60
        new_m = result % 60
        return Time(new_h , new_m)

    def sub(self , time):
        result = self.h * 60 + self.m - (time.h * 60 + time.m)
        new_h = result // 60
        new_m = result % 60
        return Time(new_h , new_m)
    
a = int(input("Enter hour of first time: "))
b = int(input("Enter minute of first time: "))
c = int(input("Enter hour of second time: "))
d = int(input("Enter minute of second time: "))

t1 = Time(a , b)
t2 = Time(c , d)

result_sum = t1.sum(t2)
result_sum.show()

result_sub = t1.sub(t2)
result_sub.show()

user_choice = int(input("What do you want? 1-time to second    2-second to time:   "))
if user_choice == 1:
    ask_user = int(input("Which one do you want to turn into seconds?  1-t1   2-t2:   "))
    if ask_user == 1:
        time_sec1 = t1.time_to_sec()
        print(t1 , "in seconds =" , time_sec1)
    elif ask_user == 2:
        time_sec2 = t2.time_to_sec()
        print(t1 , "in second =" , time_sec2)
    else:
        print("Invalid number!")
elif user_choice == 2:
    seconds = int(input("Enter a number: "))
    user_int = Time.second_to_time(seconds)
    user_int.show()
else:
    print("Invalid number!")
