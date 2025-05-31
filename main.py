n = int(input("Enter a random string of numbers: "))
num = n
res = 0
while num != 0:
    a = num%10
    res = res * 10 + a
    num = num // 10

print(res)