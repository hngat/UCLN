from billList import *
BList = BillList() #tạo một đối tượng mới của lớp "BillList" và gán cho biến "BList".
n=int(input("Nhập số hóa đơn muốn nhập"))
for i in range (n):
    bill1 = Bill()
    mabill = input("Nhập vào mã bill")
    ngaynhap = input("Nhập ngày bán, chú ý theo định dạng dd-mm-yyyy")
    mahangban = input("Nhập mã hàng cần bán")
    soluonghang = input("Nhập số lượng hàng")
    dongiahang = input("Nhập đơn giá hàng hóa")
    idnm= input("Nhập ID của khách hàng")
    idnb = input("Nhập ID của nhân viên")
    bill1.nhapBill(mabill,ngaynhap, mahangban,soluonghang,dongiahang,idnm, idnb)
    BList.thembill(bill1)
print(BList.xuat())
BList.xuattofile('billdata')




