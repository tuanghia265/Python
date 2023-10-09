n = int(input("Nhập số phần tử: "))
myArr = []
for i in range(n):
    myArr.append(int(input(f"Số thứ {i+1}: ")))

so = int(input("Nhập số muốn tìm: "))
count = 0
for i in myArr:
    if i == so:
        count += 1
if count > 0:
    print(f"Có số {so} trong dãy")
else:
    print(f"Không có số {so} trong dãy")

