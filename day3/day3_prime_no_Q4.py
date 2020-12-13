prime=2
counter = 0
x = int(input("Enter count of prime number:\n"))
while (counter < x):
    if all(prime % j != 0 for j in range(2, prime)):
        print(prime, "is a prime number")
        counter += 1


    prime += 1