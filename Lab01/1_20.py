def ChuoiCuaToi(myStr, n):
    kq = ""
    for i in range(n):
        kq += myStr
    return kq

myStr = str(input("Mời nhập chuỗi: "))
n = int(input("Nhập số lần muốn xuất: "))
kq = ChuoiCuaToi(myStr, n)
print(kq)