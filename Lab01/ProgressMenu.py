import os
import time
import XuLy1 as ChucNang
import msvcrt as m
import random
import Bai2_12 as Cau12

def DSMenu():
    print("""
        1. Tính:
            a) (a + b),
            b) a/b,
            c) a^b
        2. Tính diện tích hình chữ nhật khi biết bán kính
        3. Xuất tất cả các số nguyên tố trong 1 khoảng cho trước
        4. Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không
        5. Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)
        6. Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)
        7. Tính tổng căn bậc 2 của n số nguyên đầu tiên
        8. Giải phương trình bậc 2: ax2 + bx + c=0
        9. Tính n!
        10.In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)
        11. Đổi giờ - phút – giây: thời gian đầu vào là giây được đổi thành giờ, phút, giây.
            Xuất kết quả ra màn hình dưới dạng: giờ:phút:giây. Ví dụ: soGiay = 3770 thì xuất
            ra màn hình 1:2:50.
        12.Cho một mảng số nguyên: (nên viết 2-3 cách)
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

def XuLyMenu():
    DSMenu()
    chon = int(input(f"Nhập số từ [0..12] để chọn chức năng (Nhấn 0 để thoát): "))
    while True:
        if chon == 0:
            os.system('cls')
            exit(0)
        elif chon ==  1:
            os.system('cls')
            print("""
                1. Tính:
                a) (a + b),
                b) a/b,
                c) a^b     
            """)
            a = int(input("Mời nhập số thứ nhất: "))
            b = int(input("Mời nhập số thứ hai: "))
            ChucNang.Tinh_a_b(a, b)
            m.getch()
            XuLyMenu()
        elif chon == 2:
            os.system('cls')
            print("2. Tính diện tích hình chữ nhật khi biết bán kính")
            a = int(input("Mời nhập chiều dài:"))
            b = int(input("Mời nhập chiều rộng: "))
            kq = ChucNang.TinhDTHCN(a, b)
            print(f"Diện tích hình chữ nhật có chiều dài {a} và chiều rộng {b} là {kq}")
            m.getch()
            XuLyMenu()
        elif chon == 3:
            os.system('cls')
            print("3. Xuất tất cả các số nguyên tố trong 1 khoảng cho trước")
            n = int(input("Nhập khoảng: "))
            ChucNang.XuatSoNguyenToTrongKhoang_n(n)
            m.getch()
            XuLyMenu()
        elif chon == 4:
            os.system('cls')
            print("4. Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không")
            n = int(input("Mời nhập số: "))
            ChucNang.KiemTraSoFibonacci(n)
            m.getch()
            XuLyMenu()
        elif chon == 5:
            os.system('cls')
            print("5. Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)")
            n = int(input("Mời nhập số thứ: "))
            print("ĐỆ QUY")
            print(f"Số Fibonacci thứ {n}: {ChucNang.TimSoFibonacciThu_n_DeQuy(n)}")
            print("KHÔNG ĐỆ QUY")
            print(f"Số Fibonacci thứ {n}: {ChucNang.TimSoFibonacciThu_n_KhongDeQuy(n)}")
            m.getch()
            XuLyMenu()
        elif chon == 6:
            os.system('cls')
            print("6. Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)")
            m.getch()
            XuLyMenu()
        elif chon == 7:
            os.system('cls')
            print("7. Tính tổng căn bậc 2 của n số nguyên đầu tiên")
            n = int(input("Mời nhập số số nguyên: "))
            kq = ChucNang.TinhTongCanBac_2_Cua_n_SoNguyen(n)
            print(f"Tổng căn bậc 2 của {n} số nguyên đầu tiên: {kq}")
            m.getch()
            XuLyMenu()
        elif chon == 8:
            os.system('cls')
            print("8. Giải phương trình bậc 2: ax2 + bx + c=0")
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            c = int(input("Nhập c: "))
            ChucNang.GiaiPTB2(a, b, c)
            m.getch()
            XuLyMenu()
        elif chon == 9:
            os.system('cls')
            print("9. Tính n!")
            n = int(input("Nhập n: "))
            kq = ChucNang.GiaiThua(n)
            print(f"n! = {kq}")
            m.getch()
            XuLyMenu()
        elif chon == 10:
            os.system('cls')
            print("10.In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)")
            m.getch()
            XuLyMenu()
        elif chon == 11:
            os.system('cls')
            print("""
                11. Đổi giờ - phút – giây: thời gian đầu vào là giây được đổi thành giờ, phút, giây.
            Xuất kết quả ra màn hình dưới dạng: giờ:phút:giây. Ví dụ: soGiay = 3770 thì xuất
            ra màn hình 1:2:50.     
            """)
            giay = int(input("Mời nhập số giây: "))
            ChucNang.DoiGio_Phut_Giay(giay)
            m.getch()
            XuLyMenu()
        