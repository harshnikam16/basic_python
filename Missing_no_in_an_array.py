def missin_value(n, array):
    array_c = set(range(1, n+1))
    empty_c = set(array)
    diff = array_c - empty_c
    if missin_value:
        print("missing number is: ", sorted(diff))
    else:
        print("Works Well", sorted(array_c))

n = int(input("Enter a number:"))
array = list(map(int, input("Enter the numbers seperated by space").split()))

missin_value(n,array)
