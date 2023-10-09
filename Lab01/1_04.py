def TinhDTHinhTron(r):
    return r*r*3.14

r = float(input("Nhập bán kính: "))
while r < 0:
    r = float(input("Phải là số dương, mời nhập lại: "))
kq = TinhDTHinhTron(r)
print(f"Diện tích hình tròn bán kính {r} là: {kq}")