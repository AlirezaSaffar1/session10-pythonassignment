class Date:
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def show(self):
        return f"{self.y}-{self.m}-{self.d}"

    def get_month_name(self):
        month_names = ["farvardin", "ordibehesth", "khordad", "tir", "mordad", "shahrivar",
            "mehr", "aban", "azar", "dey", "bahman", "esfand"]
        return month_names[self.m - 1]

    def sum(self, other_date):
        carry = 0

        new_day = self.d + other_date.d
        if new_day > 30:
            new_day -= 30
            carry = 1

        new_month = self.m + other_date.m + carry
        if new_month > 12:
            new_month -= 12
            carry = 1
        else:
            carry = 0

        new_year = self.y + other_date.y + carry
        return Date(new_year, new_month, new_day)

    def sub(self, other_date):
        year_diff = self.y - other_date.y
        month_diff = self.m - other_date.m
        day_diff = self.d - other_date.d

        if day_diff < 0:
            month_diff -= 1
            day_diff += 30

        if month_diff < 0:
            year_diff -= 1
            month_diff += 12
            return Date(year_diff, month_diff, day_diff)

a = int(input("enter the 1st date year = "))
b = int(input("enter the 1st date month = "))
c = int(input("enter the 1st date day = "))
d = int(input("enter the 2nd date year = "))
e = int(input("enter the 2nd date month = "))
f = int(input("enter the 2nd date day = "))

date1 = Date(a, b, c)
date2 = Date(d, e, f)

option=int(input("What do you want: 1-add   2-subtract   3-month name:  "))
if option==1:
    result_add = date1.sum(date2)
    print(f" {date1} + {date2} = {result_add}")
elif option==2:
    result_subtract = date1.sub(date2)
    print(f"{date1} - {date2} = {result_subtract}")
elif option==3:
    month_name = date1.get_month_name()
    print(f"Month Name: {month_name}")
else:
    print("Invalid number!")