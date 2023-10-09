def is_vowel(kt):
    all_vowels = 'aeiou'
    return kt in all_vowels
kt = str(input("Nhập ký tự để kiểm tra: "))
kq = is_vowel(kt)
print(kq)

    