from bill import *
class BillList():
    list = []
    tongsobill = 0
    def __init__(self): #Phương thức khởi tạo __init__() khởi tạo lại biến list và biến tongsobill để đảm bảo
        # rằng chúng được khởi tạo là rỗng và 0 mỗi khi một đối tượng BillList mới được tạo ra.
        self.list = []
        self.tongsobill= 0
    def thembill(self,b):
        self.list.append(b)
        self.tongsobill+=1
    def doctufile(self,tenfile):
        pass
    def xuat(self):
        S = ' '
        for bi in self.list:
            S+=bi.xuattrachuoi() + '\n'
        return S
    def xuattofile(self,tenfile):
        fh=open(tenfile, 'a+') # mở tệp tin với chế độ 'a+', mở tệp tin để ghi thêm vào cuối tệp nếu tệp tin đã tồn tại hoặc tạo một tệp tin mới nếu tệp tin chưa tồn tại
        for bi in self.list: #Vòng lặp for duyệt qua các phần tử trong danh sách, gọi phương thức xuattrachuoi() của từng đối tượng để chuyển đối tượng thành một chuỗi ký tự và ghi vào tệp tin bằng phương thức write()
            fh.write(bi.xuattrachuoi()+'\n')
        fh.close() #đóng tệp tin đã được mở để giải phóng tài nguyên và lưu lại các thay đổi vào tệp tin.




