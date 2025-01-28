def sum_of_even_numbers(n):
   
    total = 0
    for num in range(2, n + 1, 2):  
        total += num
    return total
n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    result = sum_of_even_numbers(n)
    print(f"The sum of all even numbers between 1 and {n} is: {result}")