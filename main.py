
# 6-m
class Telefon:
    def yoq(self):
        print(f'telefon yoqildi')

    def qongiroq(self):
        self.yoq()
        print(f'qoniroq qilinyapti')

    def ochir(self):
        self.qongiroq()
        print(f'telefon ochirildi')

t1 = Telefon()
t1.yoq()
t1.qongiroq()
t1.ochir()



# 7-m
class Kitob:
    def och(self):
        print(f'kitob ochildi')

    def oqi(self):
        self.och()
        print(f'kitob oqilmoqda')

    def yop(self):
        self.oqi()
        print(f'kitob yopildi')

k1 = Kitob()
k1.och()
k1.oqi()
k1.yop()

# 8-m
class ovqat:
    def tayyorla(self):
        print(f'ovqat tayyorlandi')

    def ye(self):
        self.tayyorla()
        print(f'ovqat yeyildi')

    def yuv(self):
        self.ye()
        print(f'idishlar yuvuldi')

o1 = ovqat()
o1.tayyorla()
o1.ye()
o1.yuv()


# 9-m
class Dars:
    def boshlash(self):
        print(f'dars boshlandi')

    def tushuntirildi(self):
        self.boshlash()
        print(f'mavzu tushuntirildi')

    def yakunlash(self):
        self.tushuntirildi()
        print(f'dars tugadi')

d1 = Dars()
d1.boshlash()
d1.tushuntirildi()
d1.yakunlash()

# 10-m
class kompyuter:
    def yoq(self):
        print(f' kompyuter yoqildi')

    def ishla(self):
        self.yoq()
        print(f'kompyuter ishlamoqda')

    def ochir(self):
        self.ishla()
        print(f'kompyuter ochirildi')

k1 = kompyuter()
k1.yoq()
k1.ishla()
k1.ochir()
