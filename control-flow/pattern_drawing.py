number = int(input("Enter the size of the pattern:"))

n = 0
while n < number:
    for j in range(number):
        print("*", end=" ")
    print()
    n += 1
        
