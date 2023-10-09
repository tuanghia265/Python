def ChuoiCuaToi(myStr):
    if len(myStr) >= 2 and myStr[:2] == "Is":
        return myStr
    else:
        return "Is" + myStr

myStr = str(input("Mời bạn nhập chuỗi: "))
kq = ChuoiCuaToi(myStr)
print(kq)