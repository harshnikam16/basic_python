def single_sum(n):
    while n >= 10:
        sum_digits = 0
        while n > 0:
            sum_digits += n % 10
            n //= 10
        n = sum_digits
    return n
    
num = int(input("Enter a num: "))
output = single_sum(num)

print ("Answer",output)
