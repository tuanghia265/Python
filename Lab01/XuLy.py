def KiemTraSoLe(so):
    if so % 2 != 0:
        return False
    else:
        return True

def KiemTraSoFibonacci(so):
    if so == ((so - 1) + (so - 2)):
        return True
    else:
        return False

def KiemTraSoNguyenTo(so):
    count = 0
    if so < 2:
        return False
    for i in range(2, so):
        if so % i == 0:
            count += 1
        
    if count > 0:
        return False
    else:
        return True
    
def TongCacChuSo(so):
    sum = 0
    so = abs(so)
    while so / 10 > 0:
        sum += (so % 10)
        so //= 10
    return sum
