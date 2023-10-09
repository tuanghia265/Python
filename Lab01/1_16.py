def TinhToan(so):
    if so <= 17:
        return 17 - so
    else:
        return (so - 17) * 2 

so = int(input("Mời bạn nhập số: "))
kq = TinhToan(so)
print(f"Kết quả: {kq}")