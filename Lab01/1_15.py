def TinhTheTichHinhCau(r):
    return (3/4)*3.14*r*r*r

r = float(input("Mời nhập bán kính: "))
kq = TinhTheTichHinhCau(r)
print(f"Thể tích của hình cầu bán kính {r} là: {kq}")