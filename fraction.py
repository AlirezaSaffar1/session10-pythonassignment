class Fraction:
    def __init__(self, s, m):
        self.s = s
        self.m = m

    def show(self):
        print(self.s , "/" , self.m)

    def mul(self , f):
        result = Fraction(None , None)
        result.s = self.s * f.s
        result.m = self.m * f.m
        return result
    
    def sum(self , f):
        result = Fraction(None , None)
        result.s = (self.s * f.m) + (self.m * f.s)
        result.m = self.m * f.m
        return result
    
    def divide(self , f):
        result = Fraction(None , None)
        result.s = self.s * f.m
        result.m = self.m * f.s
        return result

    def sub(self , f):
        result = Fraction(None , None)
        result.s = (self.s * f.m) - (self.m * f.s)
        result.m = self.m * f.m
        return result

a = float(input("Soorat kasr aval: "))
b = float(input("Makhraj kasr aval: "))
c = float(input("Soorat kasr dovom: "))
d = float(input("Makhraj kasr dovom: "))

f1 = Fraction(a , b)
f2 = Fraction(c , d)

f1.show()
f2.show()

result_m = f1.mul(f2)
result_m.show()

result_sum = f1.sum(f2)
result_sum.show()

result_d = f1.divide(f2)
result_d.show()

result_sub = f1.sub(f2)
result_sub.show()