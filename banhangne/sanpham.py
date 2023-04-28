from productlist import *
SPlist = Productlist()
n=int(input("Nhập số san pham muốn nhập"))
for i in range (n):
    SP = Product()
    IDSP= input("Nhập vào mã ID sản phẩm")
    tensp = input("Nhập vào tên sản phẩm")
    giasp = input("Nhập vào giá sản phẩm")
    soluongsp = input("Nhập vào số lượng sản phẩm")
    SP.addinfor(IDSP,tensp,giasp,soluongsp)
    SPlist.themsanpham(SP)

print(SPlist.printtoscreen())
SPlist.savetofile('Danhmucsp.dataa')