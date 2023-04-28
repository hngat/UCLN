import tkinter as tk
from billList import *

Billlist = BillList() #tạo một đối tượng mới của lớp "BillList" và gán cho biến "Billlist".
def hamxuly():
    bill = Bill()
    id=idtxtbox.get()
    ngay=ngaytxtbox.get()
    mahang=mahangtxtbox.get()
    soluonghang=int(soluonghangtxtbox.get())
    dongiahang=int(dongiahangtxtbox.get())
    idnm=idnmtxtbox.get()
    idnb=idnbtxtbox.get()
    bill.nhapBill(id,ngay,mahang,soluonghang,dongiahang,idnm,idnb)
    #bill.xuattrachuoi()
    Billlist.thembill(bill)
    Billlist.xuattofile('billdata')

def another_button_():
    idtxtbox.delete(0, tk.END)
    ngaytxtbox.delete(0, tk.END)
    mahangtxtbox.delete(0, tk.END)
    soluonghangtxtbox.delete(0, tk.END)
    dongiahangtxtbox.delete(0, tk.END)
    idnmtxtbox.delete(0, tk.END)
    idnbtxtbox.delete(0, tk.END)

giaodien=tk.Tk() #tạo một đối tượng giao diện người dùng  và đặt tên cho nó là "giaodien"
giaodien.geometry('400x400') #sử dụng để thiết lập kích thước của cửa sổ là 400x400 pixel.
giaodien.title('Nhập hóa đơn') # được sử dụng để đặt tiêu đề cho cửa sổ là "Nhập hóa đơn".
#tạo ra các đối tượng trên giao diện
idlable=tk.Label(giaodien,text = 'Nhập ID') #Tạo một nhãn (label) được đặt tên là "idlable" với nội dung là "Nhập ID" để hiển thị text
idtxtbox=tk.Entry(giaodien, width=30) #Tạo một ô nhập liệu (entry) với độ rộng là 30 để tạp nhập texxt
ngaylable =tk.Label(giaodien, text = "Ngày nhập")
ngaytxtbox = tk.Entry(giaodien,width = 30)
mahanglable =tk.Label(giaodien, text = "Mã hàng")
mahangtxtbox = tk.Entry(giaodien,width = 30)
soluonghanglable =tk.Label(giaodien, text = "Số lượng")
soluonghangtxtbox = tk.Entry(giaodien,width = 30)
dongiahanglable =tk.Label(giaodien, text = "Đơn giá")
dongiahangtxtbox = tk.Entry(giaodien,width = 30)
idnmlable =tk.Label(giaodien, text = "Người mua")
idnmtxtbox = tk.Entry(giaodien,width = 30)
idnblable =tk.Label(giaodien, text = "Người bán")
idnbtxtbox = tk.Entry(giaodien,width = 30)

submit_button=tk.Button(giaodien, text = 'Chấp nhận', command=hamxuly) #"command" là đối số truyền vào để chỉ định hàm "hamxuly" sẽ được gọi khi người dùng nhấn nút.
another_button=tk.Button(giaodien, text = 'Thêm mới', command=another_button_)


#Hiện ra
idlable.place(x=60, y=100)
ngaylable.place(x=60,y=130)
mahanglable.place(x=60, y=160)
soluonghanglable.place(x=60,y=190)
dongiahanglable.place(x=60,y=220)
idnmlable.place(x=60,y=250)
idnblable.place(x=60,y=280)
idtxtbox.place(x=140,y=100)
ngaytxtbox.place(x=140,y=130)
mahangtxtbox.place(x=140,y=160)
soluonghangtxtbox.place(x=140,y=190)
dongiahangtxtbox.place(x=140,y=220)
idnmtxtbox.place(x=140,y=250)
idnbtxtbox.place(x=140,y=280)
submit_button.place(x=130,y=330)
another_button.place(x=220, y=330)


#kqtxtbox.place(x=180, y =200)

giaodien.mainloop()



# kqtxtbox.delete(0,tk.END)
# kqtxtbox.insert(0,Billlist.xuat()
#kqlable =tk.Label(giaodien, text = "Tổng hop")
#kqtxtbox = tk.Entry(giaodien,width = 30)