from product import *
class Productlist():
    danhsach = []
    tongsosanpham = 0
    def __init__(self):
        self.danhsach = []
        self.tongsosanpham = 0
    def themsanpham(self,sp):
        self.danhsach.append(sp)
        self.tongsosanpham+=1
    def printtoscreen(self):
        S= ''
        for i in self.danhsach:
            S+=i.detailtostring() + '\n'
        return S
    def savetofile(self,tenfile):
        fh = open(tenfile, 'a+')
        for i in self.danhsach:
            fh.write(i.detailtostring() + '\n')
        fh.close()