def tim_uoc_chung_lon_nhat(m, n):
    if n == 0:
        return m
    else:
        return tim_uoc_chung_lon_nhat(n, m % n)
def tim_uoc_chung_lon_nhat_ko_de_quy(m, n):
    while n != 0:
        m, n = n, m % n
    return m

# Ví dụ sử dụng
m=int(input("Nhập số m = "))
n=int(input("Nhập số n = "))
print(f"Đệ Qui Ước chung lớn nhất của {m} và {n} là: {tim_uoc_chung_lon_nhat(m, n)}")
print(f"không Đệ Qui Ước chung lớn nhất của {m} và {n} là: {tim_uoc_chung_lon_nhat_ko_de_quy(m, n)}")