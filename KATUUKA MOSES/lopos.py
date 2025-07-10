n = int(input("enter a positive number:"))

if n <= 0:
    print("enter number greater than 0")
else:
    sum_even = 0
    for i in range(1, n+1):
        if i % 2== 0:
            sum_even += i
    print ("the sum of all even numbers from 1 to", n, "is",sum_even)
     

