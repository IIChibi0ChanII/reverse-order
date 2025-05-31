n = int(input("Enter a random string of numbers: "))
num = n
res = 0
while num != 0:
    a = num%10 # gets the last number
    res = res * 10 + a # adds a 0 at the end of the result and replaces with the last number
    num = num // 10 #excludes the last number for the next calculation

print(res)