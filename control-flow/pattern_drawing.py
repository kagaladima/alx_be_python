# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer loop: controls the number of rows
while row < size:
    # Inner loop: prints asterisks for each column
    for col in range(size):
        print("*", end="")  # print without newline

    print()  # move to the next line after each row
    row += 1  # go to the next row
