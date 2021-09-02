counter: int = 0 
maximum = int(input("Count up to, but not including what: "))
while counter < maximum:
    counter_squared: int = counter ** counter
    print("The square of " + str(counter) + " is equal to " + str(counter_squared))
    counter = counter + 1