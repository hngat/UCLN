class Bill():
    BillID = 0
    ngayban = '25-4-2023'
    mahang = '0000'
    sl = 1
    dongia = 3000
    idnguoimua = 'KH01'
    idnguoiban = 'NV01'
    def __init__(self,  BillID = 0, ngayban = '25-4-2023', mahang = '0000',  sl = 1, dongia = 3000, idnguoimua = 'KH01',idnguoiban = 'NV01'):
        self.BillID = BillID
        self.ngayban = ngayban
        self.mahang = mahang
        self.sl = sl
        self.dongia=dongia
        self.idnguoimua = idnguoimua
        self.idnguoiban = idnguoiban
    def nhapBill(self, BillID, ngayban, mahang, sl, dongia,idnguoimua,idnguoiban):
        self.BillID = BillID
        self.ngayban = ngayban
        self.mahang = mahang
        self.sl = sl
        self.dongia = dongia
        self.idnguoimua = idnguoimua
        self.idnguoiban = idnguoiban
   # def nhaptuchuoi(self,chuoi,BillID, ngayban, mahang, sl, dongia,idnguoimua,idnguoiban):
       # kq=chuoi.Split('/')
        #self.BillID = BillID
        #self.ngayban = ngayban
        #self.mahang = mahang
       # self.sl = sl
       # self.dongia = dongia
       # self.idnguoimua = idnguoimua
       # self.idnguoiban = idnguoiban
    def thaydoigia(self,BillID,dongia):
        self.BillID = BillID
        self.dongia = dongia

    def xuatbill(self):
        return self.BillID,self.ngayban,self.mahang,self.sl,self.dongia, self.idnguoimua, self.idnguoiban
    def xuattrachuoi(self):
        S = str(self.BillID) + '/' + self.ngayban + '/' + self.mahang + '/' + str(self.sl) + '/' + str(self.dongia) + '/' + self.idnguoimua + '/' + self.idnguoiban
        return S

