import numpy as np

def classify_number(n):
    Uoc_so = np.arange(1, n // 2 + 1)
    Tong_cac_uoc = np.sum(Uoc_so[n % Uoc_so == 0])
    if Tong_cac_uoc < n:
        return "deficient"
    elif Tong_cac_uoc == n:
        return "perfect"
    else:
        return "abundant"

def Number(x, y):
    if x <= 0 or y <= 0:
        print("x và y phải là số nguyên dương.")
        return
    elif x > y:
        print("x phải nhỏ hơn hoặc bằng y.")
        return
    print("Phân loại các số từ", x, "đến", y, ":")
    for num in range(x, y + 1):
        print(f"Số {num} là {classify_number(num)}")

x = int(input("Nhập số nguyên dương x: "))
y = int(input("Nhập số nguyên dương y (x ≤ y): "))
Number(x, y)