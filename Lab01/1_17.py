def KiemTra(so):
    if (1000-so) <= 100 or (2000-so) <= 100:
        return True
    else:
        return False

so = int(input("Mời nhập số: "))
kq = KiemTra(so)
print(kq)