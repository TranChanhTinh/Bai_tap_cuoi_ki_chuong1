def Neper(n):
    assert n >= 0 and int(n) == n
    sum = 0
    factorial = 1
    for k in range(n + 1):
        sum += 1 / factorial
        factorial *= (k + 1)  # Tính giai thừa của k + 1 để sử dụng cho a_k+1

    return sum

n = int(input("Nhập số nguyên n (n ≥ 0): "))
print("Tổng của các số hạng từ a0 đến an là:", Neper(n))
