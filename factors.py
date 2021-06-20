# taking input from the user
positive_intiger = int(input("Enter a positive integer:"))


# function to find out and print the factors of the given positive_integer
def print_factors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            print(i, " is a factor of ", positive_intiger)


print_factors(positive_intiger)
