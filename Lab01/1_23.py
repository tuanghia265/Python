def ChuoiCuaToi(myStr, n):
    if len(myStr) >= 2:
        return myStr[:2]*n
    else:
        return myStr*n

myStr = str(input("Mời nhập chuỗi: "))
n = int(input("Nhập số lần muốn xuất: "))
kq = ChuoiCuaToi(myStr, n)
print(kq)