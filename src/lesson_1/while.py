x = float(input("Give me a positive number: "))

old = 0.0
guess = 1.0

while guess != old:
    old = guess
    guess = (guess + x/guess)/2

print(f"The square root of {x} is {guess}.")
