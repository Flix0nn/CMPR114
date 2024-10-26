def print_odd_even(max):
    for num in range(1, max + 1):
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

print_odd_even(10)