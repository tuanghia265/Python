def TinhToan(a, b, c):
    if a==b and a==c:
        return 3 * (a + b + c)
    else:
        return a + b + c

a = int(input("Số thứ nhất: "))
b = int(input("Số thứ hai: "))
c = int(input("Số thứ ba: "))
kq = TinhToan(a, b, c)
print(f"Kết quả của 3 số {a}, {b}, {c} là: {kq}")