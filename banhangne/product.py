class Product():
    ID = '00' #ID: một chuỗi ký tự có giá trị mặc định là "00".
    name = ''
    price = 100 #một số nguyên để lưu giá của sản phẩm, giá trị mặc định là 100.
    itemnum = 0
    # Những dòng code này định nghĩa các thuộc tính mặc định cho lớp "Product". Khi một đối
    #tượng (object) được tạo từ lớp này, các thuộc tính này sẽ được sử dụng cho đối tượng đó, trừ
  # khi giá trị được cung cấp cho các thuộc tính này trong quá trình tạo đối tượng.
    def __init__(self,ID='00', name = '', price = 100, itemnum = 0): #khởi tạo, xây dựng các thuộc tính của lớp đối tượng (những thông tin, đặc điểm của đối tượng)
        self.ID = ID #self,các tham số ứng với các thuộc tính.
        self.name = name #self.thuộc tính name = tham số name
        self.price = price
        self.itemnum = itemnum
    def addinfor(self, ID='00', name = '', price = 100, itemnum = 0 ): #xây dựng phương thưc bao gồm những thao tác có thể thực hiện trên lớp đối tượng
        self.ID = ID
        self.name = name
        self.price = price
        self.itemnum = itemnum
    def addprice(self, price):
        self.price=price
    def addnumber(self,n):
        self.itemnum=n
    def increasenumber(self,n):
        self.itemnum+=n
    def decreasenumber(self,n):
        self.itemnum-=n

    def detailoutput(self):
        return self.ID, self.name, self.price, self.itemnum
    def idoutput(self):
        return self.ID
    def detailtostring(self):
        return str(self.ID) + '/' + str(self.name)+ '/'  + str(self.price) + '/' + str(self.itemnum)

#lập trifnh hướng đối tượng là ktlt lấy đối tượng làm nền tang để xây dựng chương trình dựa trên kiến trúc lopws và đối tượng
#Đối tượng là thực thể thể hiện dựa trên khuôn mẫu của Lớp. gồm thuộc tính: những thông tin đặc điểm của đối tượng và phương trhucws: những thao tác, hh động mà đối tượng có thể thực hiện
#Lớp: là khuôn mẫu, là sự kết hợp giữa các thuộc tính và phương thức, các đối tượng có đặc tính tương tự tạo thành một lớp