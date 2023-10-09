n = int(input("Nhập số phần tử: "))
count = 0
for i in range(n):
    i = int(input(f"Số thứ {i+1}: "))
    if i == 4:
        count += 1
if count > 0:
    print(f"Có {count} số 4 trong dãy")
else:
    print(f"Không số 4 trong dãy")


