import math

def Tinh_a_b(a, b):
    print(f"{a} + {b} = {a+b}")
    print(f"{a} / {b} = {round(a/b, 3)}")
    print(f"{a}^{b} = {pow(a, b)}")
    
def TinhDTHCN(a, b):
    return a * b

def KiemTraSoNguyenTo(so):
    count = 0
    if so < 2:
        return False
    i = 2
    while i < so:
        if so % i == 0:
            count += 1
        i += 1
        
    if count > 0:
        return False
    else:
        return True

def XuatSoNguyenToTrongKhoang_n(n):
    arr =  []
    for i in range(n+1):
        if KiemTraSoNguyenTo(i) == True:
            arr.append(i)
    print(f"Dãy số nguyên tố trong khoảng từ 0 tới {n}: {arr}")
    
def KiemTraSoFibonacci(n):
    if n == ((n-1) + (n-2)):
        print(f"{n} là số Fibonacci")
    else:
        print(f"{n} không phải số Fibonacci")
    
def TimSoFibonacciThu_n_DeQuy(n):
    if n == 1 or n == 2:
        return 1
    return TimSoFibonacciThu_n_DeQuy(n-1) + TimSoFibonacciThu_n_DeQuy(n-2)
    
def TimSoFibonacciThu_n_KhongDeQuy(n):
    a = 1
    b = 1
    kq = 0
    i = 3
    if n == 1 or n == 2:
        return 1
    while i <= n:
        kq  = a + b
        a = b
        b = kq
        i += 1
    return kq 

def TinhTongCanBac_2_Cua_n_SoNguyen(n):
    sum = 0
    for i in range(n+1):
        sum += round(math.sqrt(i),2)
    return sum

def GiaiPTB2(a, b, c):
    delta = b*b - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm!")
    elif delta == 0:
        print(f"x1 = x2 = {(-b)/(2*a)}")
    else:
        print(f"""
            x1 = {(-b + math.sqrt(delta))/(2*a)}
            x2 = {(-b - math.sqrt(delta))/(2*a)}      
        """)
        
def GiaiThua(n):
    if n == 0:
        return 1
    return n * GiaiThua(n-1)

def DoiGio_Phut_Giay(giay):
    gio = giay // 3600
    phut = (giay % 3600)//60
    giay = giay - (gio * 3600 + phut * 60)
    print(f"{gio} : {phut} : {giay}")