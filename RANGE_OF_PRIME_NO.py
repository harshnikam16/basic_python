a = int(input("Enter the start: "))
b = int(input("Enter the end: "))

print("No.s are: ")

for i in range (a, b + 1):
    if i > 1:
        is_prime = True
        for c in range (2,i):
            if i % c == 0:
                is_prime = False
        if is_prime:
            print (i)
