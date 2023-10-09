import random
import msvcrt as m
import os
import time
import XuLy as Cau12

def XuatMenu_12():
    print("""
        a) Xuât tất cả các số lẻ không chia hết cho 5
        b) Xuất tất cả các số Fibonacci
        c) Tìm số nguyên tố lớn nhất
        d) Tìm số Fibonacci bé nhất
        e) Tính trung bình các số lẻ
        f) Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng
        g) Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ
        h) Đảo ngược trật tự các phần tử của danh sách
        i) Xuất tất cả các số lớn thứ nhì của danh sách
        j) Tính tổng các chữ số của tất cả các số trong danh sách
        k) Đếm số lần xuất hiện của một số trong danh sách
        l) Xuất các số xuất hiện n lần trong danh sách
        m) Xuất các số xuất hiện nhiều lần nhất trong danh sách  
    """)
arr = []
n = int(input("Nhập số số nguyên trong mảng: "))
for i in range(n):
    i = random.randint(-100, 100)
    arr.append(i)
print("Nhấn ENTER để tạo mảng số nguyên!")
m.getch()
print(f"Đã tạo mảng thành công, mảng số nguyên vừa tạo: {arr}")
m.getch()
def XuLyMenu_12():
    XuatMenu_12()
    
    choice = str(input("Nhập từ [a..m] để chọn chức năng (Nhấn 0 để thoát): "))
    while True:
        if choice == '0':
            os.system('cls')
            exit(0)
        elif choice == 'a':
            os.system('cls')
            print("a) Xuât tất cả các số lẻ không chia hết cho 5")
            arr_2 = []
            for i in arr:
                if Cau12.KiemTraSoLe(i) == True and i % 5 != 0:
                    arr_2.append(i)
            print(f"Các số lẻ không chia hết cho 5 là: {arr_2}")
            m.getch()
            os.system('cls')
            XuLyMenu_12()
        elif choice == 'b':
            os.system('cls')
            print("b) Xuất tất cả các số Fibonacci")
            arr_2 = []
            for i in arr:
                if Cau12.KiemTraSoFibonacci(i) == True:
                    arr_2.append(i)
            if len(arr_2) == 0:
                print("Không có số Fibonacci trong mảng")
                m.getch()
                os.system('cls')
                XuLyMenu_12()
            else:
                print(f"Các số Fibonacci trong mảng: {arr_2}")
            m.getch()
            os.system('cls')
            XuLyMenu_12()
        elif choice == 'c':
            os.system('cls')   
            print("c) Tìm số nguyên tố lớn nhất")
            arr_2 = []
            for i in arr:
                if Cau12.KiemTraSoNguyenTo(i) == True:
                    arr_2.append(i)
            max = arr_2[0]
            for i in arr_2:
                if i > max:
                    max = i
            print(f"Số nguyên tố lớn nhất là: {max}")
            m.getch()
            os.system('cls')
            XuLyMenu_12()
        elif choice == 'd':
            os.system('cls')   
            print("d) Tìm số Fibonacci bé nhất")
            arr_2 = []
            for i in arr:
                if Cau12.KiemTraSoFibonacci(i) == True:
                    arr_2.append(i)
            if len(arr_2) == 0:
                print("Không có số Fibonacci trong mảng")
                m.getch()
                os.system('cls')
                XuLyMenu_12()
            min = arr_2[0]
            for i in arr_2:
                if i < min:
                    min = i
            print(f"Số Fibonacci nhỏ nhất là: {min}")
            m.getch()
            os.system('cls')
            XuLyMenu_12()
        elif choice == 'e':
            os.system('cls') 
            print("e) Tính trung bình các số lẻ")
            arr_2 = []
            count = 0
            for i in arr:
                if Cau12.KiemTraSoLe(i) == True:
                    arr_2.append(i)
                    count += 1
            sum = 0
            for i in arr_2:
                sum += i
            print(f"Trung bình cộng các số lẻ trong mảng là: {round((sum/count), 2)}")
            m.getch()
            os.system('cls')
            XuLyMenu_12()
        elif choice == 'f':
            os.system('cls')
            print("f) Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng")
            arr_2 = []
            for i in arr:
                if Cau12.KiemTraSoLe(i) == True and i % 3 != 0:
                    arr_2.append(i)
            if len(arr_2) == 0:
                print("Không có số lẻ nào không chia hết cho 3")
            else:
                tich = 1
                for i in arr_2:
                    tich *= i
                print(f"Tích các số lẻ không chia hết cho 3 là: {tich}")
            m.getch()
            os.system('cls')
            XuLyMenu_12()
        elif choice == 'g':
            os.system('cls')
            print("g) Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ")
            i = int(input(f"Nhập vị trí của phần tử đầu tiên [0..{n-1}]: "))
            j = int(input(f"Nhập vị trí của phần tử thứ hai [0..{n-1}]: "))
            print(f"Mảng ban đầu: {arr}")
            emp = arr[i]
            arr[i] = arr[j]
            arr[j] = emp
            print(f"Mảng sau khi đổi vị trí giữa {i} và {j}: {arr}")
            m.getch()
            os.system('cls')
            XuLyMenu_12()
        elif choice == 'h':
            os.system('cls')
            print("h) Đảo ngược trật tự các phần tử của danh sách")
            i = -1
            arr_2 = []
            while (i - 1) >= -n-1:
                arr_2.append(arr[i])
                i -= 1
            print(f"Mảng ban đầu: {arr}")
            print(f"Mảng sau khi đảo ngược trật tự: {arr_2}")
            m.getch()
            os.system('cls')
            XuLyMenu_12()
        elif choice == 'i':
            os.system('cls')
            print("i) Xuất tất cả các số lớn thứ nhì của danh sách")
            arr_2 = []
            for i in arr:
                arr_2.append(i)
            max = arr_2[0]
            for i in arr_2:
                if i > max:
                    max = i
            for i in arr_2:
                if i == max:
                    arr_2.remove(i)
            arr_3 = arr_2
            max = arr_3[0]
            arr_4 = []
            for i in arr_3:
                if i > max:
                    max = i
            for i in arr_3:
                if i == max:
                    arr_4.append(i)
            print(arr)
            print(f"Các số lớn thứ nhì của mảng: {arr_4}")
            m.getch()
            os.system('cls')
            XuLyMenu_12()
        elif choice == 'j':
            os.system('cls')
            print("j) Tính tổng các chữ số của tất cả các số trong danh sách")
            arr_2 = []
            for i in arr:
                kq = Cau12.TongCacChuSo(i)
                arr_2.append(kq)
            print(arr)
            print(f"Tổng các chữ số của các phần tử trong mảng: {arr_2}")
            m.getch()
            os.system('cls')
            XuLyMenu_12()
        elif choice == 'k':
            os.system('cls')
            print("k) Đếm số lần xuất hiện của một số trong danh sách")
            count = 0
            print(arr)
            n = int(input("Nhập số muốn đếm: "))
            for i in arr:
                if i == n:
                    count += 1
            if count == 0:
                print(f"Không có số {n} trong mảng")
            else:
                print(f"Có {count} số {n} trong mảng")
            m.getch()
            os.system('cls')
            XuLyMenu_12()
        elif choice == 'l':
            os.system('cls')
            print("l) Xuất các số xuất hiện n lần trong danh sách")
            n =  int(input("Nhập số lần xuất hiện: "))
            while n == 0:
                n = int(input("Số lần xuất hiện phải lớn hơn 0, mời nhập lại: "))
            # i = 0
            # count = 0
            # while arr[i] < arr[len(arr)]:
            #     kt = arr[i]
            #     if arr[i] == kt:
            #         count += 1
            #         if count > n:
            #             continue
            #     i += 1
            arr_2 = []
            for i in arr:
                if arr.count(i) == n:
                    arr_2.append(i)
            if len(arr_2) == 0:
                print(f"Không có số nào hiện {n} lần trong mảng")
            else:
                print(f"Các số hiện {n} lần trong mảng: {arr_2}")
            m.getch()
            os.system('cls')
            XuLyMenu_12()
        elif choice == 'm':
            os.system('cls')
            print("m) Xuất các số xuất hiện nhiều lần nhất trong danh sách")
            arr_2 = []
            max = arr.count(arr[0])
            for i in arr:
                if arr.count(i) > max:
                    max = arr.count(i)
            for i in arr:
                if arr.count(i) == max:
                    arr_2.append(i)
            print(arr)
            print(f"Các số xuất hiện nhiều nhất trong mảng: {arr_2}")
            m.getch()
            os.system('cls')
            XuLyMenu_12()
                    
XuLyMenu_12()