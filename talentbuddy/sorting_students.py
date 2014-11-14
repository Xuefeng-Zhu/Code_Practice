def sort_students(numbers):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    changed = True 
    while changed:
        changed = False
        for i in range(1, len(numbers)):
            if numbers[i-1] > numbers[i]:
                numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
                changed = True 
    print " ".join(str(number) for number in numbers)
