# Print a upside-down Equilateral triangle
height = int(input("Enter the height of the equilateral triangle: "))

# Loop through each row
for i in range(height, 0, -1):
    # Print spaced for the left side of the triangle
    for n in range(height - i):
        print(" ", end="")
    # Print stars for the current row
    for m in range(2 * i - 1):
        print("*", end="")
    print()