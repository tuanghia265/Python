def TinhToan(so):
    return so + (so*10+so) + (so*100+so*10+so)

so = int(input("Mời bạn nhập số: "))
kq = TinhToan(so)
print(f"Kết quả: {kq}")